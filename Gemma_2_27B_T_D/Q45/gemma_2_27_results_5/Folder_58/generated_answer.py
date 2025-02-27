from itertools import permutations

def palindromes_between_indices(text):
    letters = [c for c in text[:7].lower() if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        candidate = ''.join(p)
        if candidate == candidate[::-1] and len(candidate) >= 6:
            palindromes.add(candidate)
    return palindromes