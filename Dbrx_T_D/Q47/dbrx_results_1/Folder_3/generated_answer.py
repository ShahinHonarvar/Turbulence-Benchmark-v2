import re

def palindromes_of_specific_lengths(s):
    s = s[27:96].lower()
    palindromes = {palindrome for length in range(49, 52) for i in range(len(s) - length + 1) for palindrome in [s[i:i + length]] if palindrome == palindrome[::-1] and re.fullmatch('[a-z]*', palindrome)}
    return palindromes