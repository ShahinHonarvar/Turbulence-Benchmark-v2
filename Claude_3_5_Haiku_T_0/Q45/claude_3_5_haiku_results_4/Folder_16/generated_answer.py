from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[6:10] if c.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(5, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                if list(candidate) == list(candidate)[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes