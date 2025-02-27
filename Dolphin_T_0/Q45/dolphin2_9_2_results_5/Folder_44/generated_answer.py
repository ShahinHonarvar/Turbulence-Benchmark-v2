from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:8] if c.isalpha()]
    palindromes = {''.join(p) for p in permutations(letters, 3) if p == p[::-1]}
    return palindromes