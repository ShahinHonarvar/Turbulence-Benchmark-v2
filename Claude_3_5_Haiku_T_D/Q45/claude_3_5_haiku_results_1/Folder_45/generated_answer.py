from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[5:10] if char.isalpha()]
    if len(letters) < 4:
        return set()
    palindromes = set()
    for perm in set(permutations(letters)):
        for start in range(len(perm) - 3):
            candidate = perm[start:start + 4]
            if len(candidate) >= 4:
                if list(candidate) == list(candidate)[::-1]:
                    palindromes.add(''.join(candidate))
    return palindromes