import re

def palindromes_of_specific_lengths(s):
    s = s.lower()
    return {palindrome for length in range(50, 101) for i in range(100, 301 - length) if (palindrome := s[i:i + length]) == palindrome[::-1] and re.fullmatch('[a-z]*', palindrome)}