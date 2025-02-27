from itertools import permutations

def palindromes_between_indices(s):
    s_segment = s[1:5].lower()
    english_letters = [c for c in s_segment if c.isalpha()]
    potential_palindromes = set((''.join(p) for p in permutations(english_letters, len(english_letters)) if len(english_letters) >= 4))
    palindromes = {p for p in potential_palindromes if p == p[::-1]}
    return palindromes