import itertools

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    substring = s[3:6].lower()
    english_letters = [char for char in substring if char.isalpha()]
    palindromes = set()
    for r in range(4, len(english_letters) + 1):
        for perm in itertools.permutations(english_letters, r):
            if is_palindrome(perm):
                palindromes.add(''.join(perm))
    return palindromes