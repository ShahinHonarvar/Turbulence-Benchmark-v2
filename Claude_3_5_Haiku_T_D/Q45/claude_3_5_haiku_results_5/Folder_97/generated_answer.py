from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:5] if c.isalpha()]
    unique_palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            candidate = list(perm)
            if len(candidate) >= 3 and candidate == candidate[::-1]:
                unique_palindromes.add(''.join(candidate))
    return unique_palindromes