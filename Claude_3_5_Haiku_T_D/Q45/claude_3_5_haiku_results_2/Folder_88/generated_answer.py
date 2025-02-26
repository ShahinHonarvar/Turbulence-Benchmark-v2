from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:8] if c.isalpha()]
    if len(letters) < 6:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(6, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                if list(candidate) == list(candidate)[::-1]:
                    unique_palindromes.add(''.join(candidate))
    return unique_palindromes