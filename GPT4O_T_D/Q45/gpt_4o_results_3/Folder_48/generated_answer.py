from itertools import permutations

def palindromes_between_indices(s):
    substr = s[6:9].lower()
    letters = [char for char in substr if char.isalpha()]
    if len(letters) < 2:
        return set()
    letter_permutations = set((''.join(p) for p in permutations(letters)))
    palindromes = set((p for p in letter_permutations if p == p[::-1] and len(p) >= 4))
    return palindromes