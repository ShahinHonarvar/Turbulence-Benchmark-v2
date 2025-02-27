from itertools import permutations

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[1:7] if c.isalpha()]
    if len(chars) < 7:
        return set()
    palindromes = set()
    for r in range(7, len(chars) + 1):
        for p in permutations(chars, r):
            p = ''.join(p)
            if p == p[::-1]:
                palindromes.add(p)
    return palindromes