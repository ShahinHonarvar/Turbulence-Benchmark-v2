import re

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 2, len(string) + 1):
            palindrome = string[i:j]
            if re.match('^[a-zA-Z]+$', palindrome):
                palindromes.add(palindrome)
    return palindromes