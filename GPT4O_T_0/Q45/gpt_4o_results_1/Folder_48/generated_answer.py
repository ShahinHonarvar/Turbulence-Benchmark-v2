from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[6:9].lower()
    letters = [char for char in substring if char.isalpha()]
    if len(letters) < 2:
        return set()
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes