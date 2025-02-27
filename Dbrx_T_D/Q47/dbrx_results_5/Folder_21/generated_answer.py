import re

def palindromes_of_specific_lengths(s):
    s = s[100:296].lower()
    length_range = range(136, 161)
    palindromes = {palindrome for length in length_range for i in range(len(s) - length + 1) if (palindrome := s[i:i + length]) and palindrome == palindrome[::-1] and re.fullmatch('[a-zA-Z]*', palindrome)}
    return palindromes