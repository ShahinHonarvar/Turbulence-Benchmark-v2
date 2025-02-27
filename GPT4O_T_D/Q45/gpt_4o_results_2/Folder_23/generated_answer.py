from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[:7] if c.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes