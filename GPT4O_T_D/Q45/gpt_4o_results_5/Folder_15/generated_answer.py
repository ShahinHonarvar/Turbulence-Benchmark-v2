import itertools

def palindromes_between_indices(s):
    substr = s[1:3].lower()
    english_letters = [c for c in substr if c.isalpha()]
    if len(english_letters) < 3:
        return set()
    perms = set(itertools.permutations(english_letters, len(english_letters)))
    palindromes = {''.join(p) for p in perms if ''.join(p) == ''.join(p)[::-1]}
    return {p for p in palindromes if len(p) >= 3}