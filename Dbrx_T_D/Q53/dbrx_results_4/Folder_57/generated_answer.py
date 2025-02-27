import re
from collections import defaultdict

def palindrome_of_length_at_least_n(s):

    def is_palindrome(s):
        s = ''.join((c.lower() for c in s if c.isalpha()))
        return s == s[::-1]
    palindromes = set(filter(is_palindrome, re.findall('\\w{93,}', s)))
    return {p for p in palindromes if p == p.lower()}