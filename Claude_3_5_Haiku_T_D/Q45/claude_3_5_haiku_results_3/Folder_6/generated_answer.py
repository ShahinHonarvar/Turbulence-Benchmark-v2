from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join((c.lower() for c in s[:8] if c.isalpha()))
    if len(letters) < 4:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            for i in range(length - 1):
                if perm[i] != perm[length - 1 - i]:
                    break
            else:
                palindromes.add(''.join(perm))
    return palindromes