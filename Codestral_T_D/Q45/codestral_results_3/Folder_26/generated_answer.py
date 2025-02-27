from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = s[4:7]
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes