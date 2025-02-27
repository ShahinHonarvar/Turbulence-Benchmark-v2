import re

def palindrome_of_length_n(string):
    length = 77
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - length + 1):
        substring = string[i:i + length]
        if substring == substring[::-1] and re.match('^[a-zA-Z]*$', substring):
            palindromes.add(substring)
    return palindromes