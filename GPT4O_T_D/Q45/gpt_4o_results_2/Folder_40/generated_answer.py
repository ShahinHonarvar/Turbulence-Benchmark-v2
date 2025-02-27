from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[4:10].lower()
    letter_part = ''.join(filter(str.isalpha, s))
    perms = set(permutations(letter_part))
    palindromes = {''.join(p) for p in perms if is_palindrome(''.join(p)) and len(p) >= 7}
    return palindromes