import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    pattern = '(?=(\x08\\w{31,}\x08))'
    matches = re.findall(pattern, string)
    for match in matches:
        palindrome = match[0]
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes