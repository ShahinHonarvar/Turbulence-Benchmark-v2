import re

def palindrome_of_length_at_least_n(str):
    pattern = re.compile('\x08\\w{30,}\x08', re.IGNORECASE)
    palindromes = set()
    for match in re.findall(pattern, str):
        match = match.lower()
        if match == match[::-1]:
            palindromes.add(match)
    return palindromes