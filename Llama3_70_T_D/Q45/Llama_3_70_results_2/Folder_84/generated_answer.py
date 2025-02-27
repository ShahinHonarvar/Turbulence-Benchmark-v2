from itertools import permutations

def palindromes_between_indices(s):
    s = s[4:10].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set((''.join(p) for r in range(3, len(s) + 1) for p in permutations(s, r) if p == p[::-1]))
    return palindromes