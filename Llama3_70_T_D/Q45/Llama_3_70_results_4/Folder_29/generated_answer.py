from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    s = s[2:10]
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for r in range(6, len(s) + 1):
        for p in permutations(s, r):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes