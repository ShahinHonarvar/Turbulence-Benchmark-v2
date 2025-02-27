import re

def palindrome_of_length_n(text):
    palindromes = set()
    regex = '[a-zA-Z]{173}'
    for match in re.finditer(regex, text):
        palindrome = match.group(0)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes