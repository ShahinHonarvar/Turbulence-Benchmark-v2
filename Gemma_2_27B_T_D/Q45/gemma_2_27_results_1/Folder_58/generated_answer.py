from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[:7] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm).lower()
        if candidate == candidate[::-1] and len(candidate) >= 6:
            palindromes.add(candidate)
    return palindromes