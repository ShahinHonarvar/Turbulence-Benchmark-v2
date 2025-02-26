from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:6] if c.isalpha()]
    if len(letters) < 6:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i, len(perm)):
                candidate = perm[i:j + 1] + perm[i:j + 1][::-1]
                if len(candidate) >= 6 and candidate == candidate[::-1]:
                    unique_palindromes.add(''.join(candidate))
    return unique_palindromes