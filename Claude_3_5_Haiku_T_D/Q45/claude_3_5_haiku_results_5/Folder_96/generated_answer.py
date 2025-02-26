from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[3:9] if c.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        if len(perm) >= 6:
            for start in range(len(perm) - 5):
                test_perm = perm[start:start + 6]
                if list(test_perm) == list(test_perm)[::-1]:
                    palindromes.add(''.join(test_perm))
    return palindromes