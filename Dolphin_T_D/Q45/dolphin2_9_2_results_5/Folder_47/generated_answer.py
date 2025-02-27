import itertools

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8]]
    return set((''.join(p) for p in itertools.product(*zip(letters, reversed(letters))) if len(p) >= 5))