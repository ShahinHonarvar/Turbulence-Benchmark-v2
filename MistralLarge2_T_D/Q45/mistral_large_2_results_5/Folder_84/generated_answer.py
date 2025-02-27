from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[4:10] if c.isalpha()]
    letters_set = set((''.join(p) for i in range(3, len(letters) + 1) for p in permutations(letters, i) if ''.join(p).lower() == ''.join(p).lower()[::-1]))
    return letters_set