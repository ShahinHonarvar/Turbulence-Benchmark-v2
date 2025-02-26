from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[2:8] if char.isalpha()]
    if len(letters) < 3:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm) - 2):
            for j in range(i + 3, len(perm) + 1):
                candidate = perm[i:j]
                if candidate == candidate[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes