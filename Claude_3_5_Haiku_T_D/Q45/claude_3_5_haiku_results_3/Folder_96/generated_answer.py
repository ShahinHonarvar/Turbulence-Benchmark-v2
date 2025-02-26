from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:9] if char.isalpha()]
    if len(letters) < 6:
        return set()
    palindromes = set()
    for perm in set(permutations(letters, 6)):
        for i in range(3):
            candidate = perm[0:3 - i] + perm[3 - i:3] + perm[3:3 + i] + perm[3 + i:]
            if candidate == candidate[::-1]:
                palindromes.add(''.join(candidate))
    return palindromes