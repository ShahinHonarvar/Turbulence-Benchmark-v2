import re
import string

def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        s = ''.join((c.lower() for c in s if c in string.english_letters))
        return s == s[::-1]
    return {p for p in re.findall(f'(?={string.english_letters}+)', s) if is_palindrome(p) and len(p) >= 150}