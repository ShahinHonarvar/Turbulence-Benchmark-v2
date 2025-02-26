from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:6] if c.isalpha()]
    if len(letters) < 3:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        if len(perm) >= 3:
            for i in range(len(perm)):
                for j in range(i + 2, len(perm) + 1):
                    candidate = perm[i:j]
                    if list(candidate) == list(candidate)[::-1]:
                        unique_palindromes.add(''.join(candidate))
    return unique_palindromes