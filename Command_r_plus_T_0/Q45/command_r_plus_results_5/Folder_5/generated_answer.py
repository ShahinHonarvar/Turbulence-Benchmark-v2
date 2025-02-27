from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:9] if c.isalpha()]
    letters = [c.lower() for c in letters]
    all_permutations = permutations(letters)
    palindromes = set((''.join(p) for p in all_permutations if len(p) >= 4 and ''.join(p) == ''.join(p)[::-1]))
    return palindromes