from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:7].lower()
    palindromes = set()
    for length in range(4, len(s) + 1):
        for p in permutations(s, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes