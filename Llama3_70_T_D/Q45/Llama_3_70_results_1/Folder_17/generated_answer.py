from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = s[2:7]
    substring = ''.join(filter(str.isalpha, substring))
    palindromes = set()
    for r in range(4, len(substring) + 1):
        for p in permutations(substring, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes