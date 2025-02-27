import re

def palindrome_of_length_at_least_n(s):
    palindromes = set((match.group(0).upper() for match in re.finditer('[a-zA-Z]{100,}', s, re.IGNORECASE) if match.group(0).upper() == match.group(0)[::-1].upper()))
    return palindromes