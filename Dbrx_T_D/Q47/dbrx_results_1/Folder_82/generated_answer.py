import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(30, 301):
        for i in range(3, 300 - length + 1):
            substring = s[i:i + length].lower()
            if re.fullmatch('[a-zA-Z]*', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes