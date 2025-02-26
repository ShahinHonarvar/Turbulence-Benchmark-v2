from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[1:4] if c.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(4, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                candidate = list(perm[start:start + length])
                if candidate == candidate[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes