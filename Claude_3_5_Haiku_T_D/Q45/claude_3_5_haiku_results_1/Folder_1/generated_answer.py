from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[4:8] if c.isalpha()]
    if len(letters) < 5:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(5, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                subset = perm[start:start + length]
                if subset == subset[::-1]:
                    unique_palindromes.add(''.join(subset))
    return unique_palindromes