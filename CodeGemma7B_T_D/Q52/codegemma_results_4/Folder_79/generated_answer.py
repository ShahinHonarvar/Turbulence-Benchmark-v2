import re

def palindrome_of_length_n(text):
    lower_text = text.lower()
    pattern = '(?i)([a-z]{64})'
    palindromes = set()
    for match in re.finditer(pattern, lower_text):
        palindrome = match.group(1)
        palindromes.add(palindrome)
    return palindromes