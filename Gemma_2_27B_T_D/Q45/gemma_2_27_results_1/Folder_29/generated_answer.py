from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[2:10] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        candidate = ''.join(p).lower()
        if candidate == candidate[::-1] and len(candidate) >= 6:
            palindromes.add(candidate)
    return palindromes