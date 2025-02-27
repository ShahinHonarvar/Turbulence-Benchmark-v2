import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(100, 301 - 50):
        for j in range(50, 101):
            substring = s[i:i + j].lower()
            if substring == substring[::-1] and re.fullmatch('[a-zA-Z]*', substring):
                palindromes.add(substring)
    return palindromes