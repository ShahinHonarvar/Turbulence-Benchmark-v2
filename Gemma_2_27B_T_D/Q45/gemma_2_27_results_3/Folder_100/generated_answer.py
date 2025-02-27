from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[:6] if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        candidate = ''.join(p)
        if candidate.lower() == candidate.lower()[::-1] and len(candidate) >= 6:
            palindromes.add(candidate)
    return palindromes