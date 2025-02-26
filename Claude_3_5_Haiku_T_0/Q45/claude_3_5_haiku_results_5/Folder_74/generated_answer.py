from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[1:7] if char.isalpha()]
    if len(letters) < 6:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters, 6)):
        for i in range(3):
            if perm[i] != perm[5 - i]:
                break
        else:
            unique_palindromes.add(''.join(perm))
    return unique_palindromes