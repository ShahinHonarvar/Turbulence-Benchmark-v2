from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[6:10] if char.isalpha()]
    if len(letters) < 5:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for i in range(len(perm) - 4):
            for j in range(i + 4, len(perm) + 1):
                candidate = perm[i:j]
                if len(candidate) >= 5 and list(candidate) == list(candidate)[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes