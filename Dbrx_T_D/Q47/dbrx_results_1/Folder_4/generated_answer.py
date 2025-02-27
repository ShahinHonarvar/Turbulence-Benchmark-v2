import re

def palindromes_of_specific_lengths(text):
    substring = text[12:93]
    palindromes = {palindrome for i in range(17, 67) for palindrome in set(map(''.join, re.findall(f'.{{{i}}}', substring))) if palindrome.lower() == palindrome[::-1]}
    return palindromes