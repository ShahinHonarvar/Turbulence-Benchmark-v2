import re

def palindrome_of_length_n(string):
    palindromes = set()
    for length in range(1, 91):
        for i in range(len(string) - length + 1):
            substring = string[i:i + length]
            if substring.lower() == substring[::-1].lower() and re.fullmatch('[a-zA-Z]*', substring):
                palindromes.add(substring)
    return {palindrome for palindrome in palindromes if len(palindrome) == 90} if palindromes else set()