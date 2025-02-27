from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    subrange = s[6:9].lower()
    letters = [char for char in subrange if char.isalpha()]
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for perm in set(permutations(letters, i)):
            if perm == perm[::-1]:
                palindromes.add(''.join(perm))
    return palindromes