from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[:7] if c.isalpha()]
    if len(letters) < 7:
        return set()
    letters_lower = ''.join(letters).lower()
    palindromes = {''.join(p) for p in permutations(letters_lower, 7) if ''.join(p) == ''.join(p)[::-1]}
    return palindromes