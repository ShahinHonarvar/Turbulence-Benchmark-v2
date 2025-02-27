import re

def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(11, 98):
        for length in range(29, 63):
            if i + length <= 97:
                substring = s[i:i + length].lower()
                if re.search('[a-z]', substring) and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes