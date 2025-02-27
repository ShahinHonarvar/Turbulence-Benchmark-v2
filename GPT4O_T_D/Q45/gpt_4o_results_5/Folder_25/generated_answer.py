from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[1:5].lower()
    letters_only = ''.join(filter(str.isalpha, substring))
    if len(letters_only) < 3:
        return set()
    palindromes = set()
    for perm in permutations(letters_only):
        candidate = ''.join(perm)
        if len(candidate) >= 3 and is_palindrome(candidate):
            palindromes.add(candidate)
    return palindromes