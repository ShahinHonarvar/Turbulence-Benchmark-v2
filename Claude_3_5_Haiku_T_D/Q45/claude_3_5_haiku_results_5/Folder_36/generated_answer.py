from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[5:9] if c.isalpha()))
    if len(letters) < 3:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm)):
            for j in range(i + 3, len(perm) + 1):
                candidate = ''.join(perm[i:j])
                if candidate == candidate[::-1]:
                    unique_palindromes.add(candidate)
    return unique_palindromes