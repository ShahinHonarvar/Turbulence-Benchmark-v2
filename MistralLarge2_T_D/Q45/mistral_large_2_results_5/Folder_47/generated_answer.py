import itertools

def palindromes_between_indices(s):
    chars = [c for c in s[3:8] if c.isalpha()]
    permutations = set((''.join(p) for i in range(1, len(chars) + 1) for p in itertools.permutations(chars, i)))
    palindromes = {p for p in permutations if len(p) >= 5 and p.lower() == p.lower()[::-1]}
    return palindromes