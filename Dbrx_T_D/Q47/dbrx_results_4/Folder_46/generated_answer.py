import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(29, 63):
        for i in range(11, 98 - length):
            substring = s[i:i + length].lower()
            if re.match('^[a-z]*$', substring) and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes