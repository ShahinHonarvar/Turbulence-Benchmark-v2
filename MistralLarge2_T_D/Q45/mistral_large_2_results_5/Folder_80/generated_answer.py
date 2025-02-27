import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if c.isalpha()]
    permutations = set((''.join(p) for p in itertools.permutations(letters)))
    palindromes = {p for p in permutations if len(p) >= 7 and p.lower() == p.lower()[::-1]}
    return palindromes