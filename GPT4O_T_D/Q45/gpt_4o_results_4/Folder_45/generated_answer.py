from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substr = s[5:10].lower()
    letters = [c for c in substr if c.isalpha()]
    palindromes = set()
    for perm in set(permutations(letters)):
        for length in range(4, len(perm) + 1):
            perm_str = ''.join(perm[:length])
            if is_palindrome(perm_str):
                palindromes.add(perm_str)
    return palindromes