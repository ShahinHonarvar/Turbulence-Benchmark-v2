import re

def palindrome_of_length_at_least_n(string):
    pattern = '([a-zA-Z])\\\\1{24,}'
    palindromes = set()
    for match in re.finditer(pattern, string, re.IGNORECASE):
        palindromes.add(match.group(0))
    return palindromes