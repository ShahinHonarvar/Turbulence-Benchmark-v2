def is_palindrome(s):
    s = ''.join((c.lower() for c in s if c.lower().isalpha()))
    return s == s[::-1] and len(s) >= 3

def palindromes_between_indices(s):
    start, end = (7, 9)
    letters = ''.join((c.lower() for c in s if c.lower().isdigit() and start <= int(c) <= end))
    return {i for i in letters if is_palindrome(i)}