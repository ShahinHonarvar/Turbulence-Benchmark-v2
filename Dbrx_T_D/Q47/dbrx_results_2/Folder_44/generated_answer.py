import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(18, 99):
        for length in range(31, 52):
            substring = s[i:i + length].lower()
            if re.match('^[a-zA-Z]*$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes