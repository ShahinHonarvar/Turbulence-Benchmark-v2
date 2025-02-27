from itertools import permutations

def palindromes_between_indices(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = ''.join([c for c in text[4:9] if c.lower() in alphabet])
    palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm).lower()
        if candidate == candidate[::-1] and len(candidate) >= 6:
            palindromes.add(candidate)
    return palindromes