import re

def palindrome_of_length_at_least_n(string):
    string = string.lower()
    matches = re.findall('[a-zA-Z]{94,}', string)
    palindromes = set()
    for match in matches:
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes