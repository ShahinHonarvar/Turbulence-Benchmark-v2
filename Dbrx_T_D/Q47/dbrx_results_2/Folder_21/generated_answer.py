import re

def palindromes_of_specific_lengths(s):
    s = s[100:296].lower()
    palindromes = {palindrome for length in range(136, 161) for i in range(len(s) - length + 1) if (palindrome := s[i:i + length]) == palindrome[::-1] and re.match('^[a-zA-Z]*$', palindrome)}
    return palindromes