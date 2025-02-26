from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:7] if c.isalpha()]
    unique_palindromes = set()
    for perm_length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, perm_length)):
            if perm_length >= 3:
                for start in range(len(perm) - perm_length + 1):
                    candidate = list(perm[start:start + perm_length])
                    if candidate == candidate[::-1]:
                        unique_palindromes.add(''.join(candidate))
    return unique_palindromes