from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[6:10].lower()
    letters = [c for c in substring if c.isalpha()]
    unique_palindromes = set()

    def is_palindrome_permutation(chars):
        return chars == chars[::-1]
    for perm in permutations(letters, 4):
        if is_palindrome_permutation(perm):
            unique_palindromes.add(''.join(perm))
    return unique_palindromes