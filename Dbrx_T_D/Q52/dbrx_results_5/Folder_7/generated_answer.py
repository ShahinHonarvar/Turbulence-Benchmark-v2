import re

def palindrome_of_length_n(string, n=416):
    string = re.findall('\\b[A-Za-z]{1}\\w*', string)
    palindromes = {substring for substring in string if substring == substring[::-1] and len(substring) == n}
    return palindromes