from itertools import permutations

def palindromes_between_indices(s):
    letters = [char for char in s[:4].lower() if char.isalpha()]
    palindromes = set()
    for r in range(3, len(letters) + 1):
        for perm in permutations(letters, r):
            if ''.join(perm) == ''.join(perm)[::-1]:
                palindromes.add(''.join(perm))
    return palindromes