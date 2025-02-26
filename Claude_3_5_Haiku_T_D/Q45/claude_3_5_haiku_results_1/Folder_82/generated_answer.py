from itertools import permutations

def palindromes_between_indices(s):
    letters_in_range = ''.join((c for c in s[1:7] if c.isalpha())).lower()
    if len(letters_in_range) < 7:
        return set()
    unique_palindromes = set()
    for perm in set(permutations(letters_in_range, 7)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            unique_palindromes.add(candidate)
    return unique_palindromes