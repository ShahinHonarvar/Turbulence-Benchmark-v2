from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substring = s[1:8]
    chars = [char.lower() for char in substring if char.isalpha()]
    palindromes = set()
    for length in range(7, len(chars) + 1):
        for perm in set(permutations(chars, length)):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes