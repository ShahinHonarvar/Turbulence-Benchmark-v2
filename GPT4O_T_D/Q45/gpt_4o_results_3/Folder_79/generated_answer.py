from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    substring = s[1:8].lower()
    english_letters = [char for char in substring if char.isalpha()]
    permutations_set = set((''.join(perm) for perm in permutations(english_letters)))
    palindromes = {p for p in permutations_set if is_palindrome(p) and len(p) >= 3}
    return palindromes