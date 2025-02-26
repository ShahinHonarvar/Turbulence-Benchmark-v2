from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:8] if char.isalpha()]
    if len(letters) < 5:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(5, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                subset = perm[start:start + length]
                if list(subset) == list(subset)[::-1]:
                    unique_palindromes.add(''.join(subset))
    return unique_palindromes