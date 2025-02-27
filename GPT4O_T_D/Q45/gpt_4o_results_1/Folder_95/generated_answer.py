from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    substring = s[7:9]
    letters = [c.lower() for c in substring if c.isalpha()]
    unique_palindromes = set()
    for perm in permutations(letters):
        candidate = ''.join(perm)
        if len(candidate) >= 3 and is_palindrome(candidate):
            unique_palindromes.add(candidate)
    return unique_palindromes