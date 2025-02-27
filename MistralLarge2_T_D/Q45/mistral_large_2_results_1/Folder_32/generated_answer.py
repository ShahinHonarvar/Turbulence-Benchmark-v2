import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[1:8] if c.isalpha()]
    combinations = set((''.join(p) for p in itertools.permutations(letters)))
    palindromes = {c for c in combinations if c == c[::-1] and len(c) >= 5}
    return palindromes