from itertools import permutations

def palindromes_between_indices(s):
    letters = [char.lower() for char in s[3:10] if char.isalpha()]
    if len(letters) < 7:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters, 7)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            unique_palindromes.add(candidate)
    return unique_palindromes