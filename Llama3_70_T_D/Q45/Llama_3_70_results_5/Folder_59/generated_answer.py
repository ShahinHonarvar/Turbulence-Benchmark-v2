from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[8:10])).lower()
    if len(substring) < 2:
        return set()
    palindromes = set()
    for r in range(3, len(substring) + 1):
        for p in permutations(substring, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes