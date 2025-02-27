from itertools import permutations

def palindromes_between_indices(s):
    substring = s[4:7]
    substring = ''.join([c.lower() for c in substring if c.isalpha()])
    palindromes = set()
    for p in permutations(substring, 4):
        s = ''.join(p)
        if s == s[::-1]:
            palindromes.add(s)
    return palindromes