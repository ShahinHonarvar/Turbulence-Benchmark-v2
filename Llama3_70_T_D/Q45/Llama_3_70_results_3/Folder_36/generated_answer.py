from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = s[5:9]
    letters = [char for char in substring if char.isalpha()]
    palindromes_set = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            if perm == perm[::-1]:
                palindromes_set.add(''.join(perm))
    return palindromes_set