from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    chars = [c.lower() for c in s[2:5] if c.isalpha()]
    permuts = set((''.join(p) for p in permutations(chars) if len(p) >= 4))
    palindromes = {p for p in permuts if p == p[::-1]}
    return palindromes