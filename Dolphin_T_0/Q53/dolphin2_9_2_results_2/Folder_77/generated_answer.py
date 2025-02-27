import re

def palindrome_of_length_at_least_n(string):
    palindromes = set()
    n = 149
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            substring = string[i:j].lower()
            if re.match('^[a-zA-Z]*$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes