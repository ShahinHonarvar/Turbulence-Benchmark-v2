from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    substring = s[2:4].lower()
    letters = [c for c in substring if c.isalpha()]
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes