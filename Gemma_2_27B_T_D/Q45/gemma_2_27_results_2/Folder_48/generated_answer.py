from itertools import permutations

def palindromes_between_indices(text):
    substring = text[6:9]
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        candidate = ''.join(p).lower()
        if len(candidate) >= 4 and candidate == candidate[::-1]:
            palindromes.add(candidate)
    return palindromes