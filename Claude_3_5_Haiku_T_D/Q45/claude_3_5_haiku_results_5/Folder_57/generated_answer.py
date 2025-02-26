from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[2:6] if c.isalpha()]
    if len(letters) < 5:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters, len(letters))):
        for i in range(len(perm)):
            candidate = ''.join(perm[i:] + perm[:i])
            if candidate == candidate[::-1] and len(candidate) >= 5:
                unique_palindromes.add(candidate)
    return unique_palindromes