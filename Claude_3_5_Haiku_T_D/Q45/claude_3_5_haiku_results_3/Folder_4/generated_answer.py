from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:10] if c.isalpha()]
    if len(letters) < 7:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters)):
        if len(perm) >= 7:
            for i in range(len(perm) - 6):
                candidate = perm[i:i + 7]
                if list(candidate) == list(candidate)[::-1]:
                    unique_palindromes.add(''.join(candidate))
    return unique_palindromes