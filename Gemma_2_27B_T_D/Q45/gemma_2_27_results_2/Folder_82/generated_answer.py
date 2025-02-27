from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[1:7] if c.isalpha()]
    palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm).lower()
        if candidate == candidate[::-1] and len(candidate) >= 7:
            palindromes.add(candidate)
    return palindromes