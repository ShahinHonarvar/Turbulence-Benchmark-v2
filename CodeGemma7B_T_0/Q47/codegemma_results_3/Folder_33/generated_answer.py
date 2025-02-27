import re

def palindromes_of_specific_lengths(text):
    pattern = '(?i)([a-zA-Z]{103,158})'
    matches = re.findall(pattern, text[130:295])
    return {palindrome for palindrome in matches if palindrome == palindrome[::-1]}