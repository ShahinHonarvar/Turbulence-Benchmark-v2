from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[4:9]
    palindromes = set()
    for length in range(3, len(s) + 1):
        for perm in permutations(s, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes