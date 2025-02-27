from itertools import product

def palindromes_between_indices(s):
    letters = set(s[1:8].lower())
    result = set()
    return result if not all((c in letters for c in 'a b c d e f g'.split())) else all_palindromes(letters)

def all_palindromes(letters):
    return set((''.join(letters) / 2 + ''.join(letters) % 2 + ''.join(reversed(letters)) / 2 for letters in product(sorted(letters), repeat=7) if len(set(letters)) == 7))