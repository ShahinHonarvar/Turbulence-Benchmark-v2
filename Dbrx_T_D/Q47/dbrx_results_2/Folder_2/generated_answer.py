import re

def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(18, 37):
        for index in range(10, len(s) - length + 1):
            substring = s[index:index + length]
            if re.fullmatch('[A-Za-z]*', substring) and substring.lower() == substring.lower()[::-1]:
                result.add(substring)
    return result