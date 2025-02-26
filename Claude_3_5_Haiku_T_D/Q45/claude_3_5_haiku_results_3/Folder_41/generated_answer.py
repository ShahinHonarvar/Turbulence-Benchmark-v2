from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:4] if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in permutations(letters):
        for i in range(len(perm)):
            test_perm = list(perm[i:] + perm[:i])
            if test_perm == test_perm[::-1] and len(test_perm) >= 3:
                palindromes.add(''.join(test_perm))
    return palindromes