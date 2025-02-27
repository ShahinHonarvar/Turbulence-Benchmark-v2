import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 15, len(string) + 1):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower() and re.match('^[a-zA-Z]+$', substring):
                palindromes.add(substring)
    return palindromes