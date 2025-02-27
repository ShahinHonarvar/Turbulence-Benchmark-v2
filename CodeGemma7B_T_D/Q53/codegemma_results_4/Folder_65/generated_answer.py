import re

def palindrome_of_length_at_least_n(text):
    pattern = re.compile('[a-zA-Z]{15,}')
    matches = pattern.findall(text)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes