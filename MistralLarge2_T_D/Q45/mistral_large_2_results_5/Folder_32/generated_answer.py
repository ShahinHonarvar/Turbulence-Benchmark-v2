from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    letters = [c for c in s[1:8] if c.isalpha()]
    lower_letters = [c.lower() for c in letters]
    all_perms = set(permutations(lower_letters, 5))
    palindromes = {''.join(perm) for perm in all_perms if is_palindrome(''.join(perm))}
    return palindromes