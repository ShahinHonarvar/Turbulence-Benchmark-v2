from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 3:
        return set()
    letters = [c.lower() for c in s[1:3] if c.lower().isalpha()]
    if len(letters) < 3:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(3, len(perm) + 1):
            for combo in set(permutations(perm, length)):
                candidate = ''.join(combo)
                if candidate == candidate[::-1]:
                    unique_palindromes.add(candidate)
    return unique_palindromes