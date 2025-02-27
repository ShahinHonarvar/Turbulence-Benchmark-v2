from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:10] if c.isalpha()]
    arrangements = set((''.join(p) for p in permutations(letters)))
    palindromes = {p for p in arrangements if p == p[::-1] and len(p) >= 3}
    return palindromes