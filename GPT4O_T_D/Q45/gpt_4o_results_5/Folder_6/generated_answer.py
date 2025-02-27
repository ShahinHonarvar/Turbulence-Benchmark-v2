from itertools import permutations

def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = [char for char in s if char.isalpha()]
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for perm in set(permutations(letters, length)):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes