import re

def palindromes_of_specific_lengths(s):
    s = s[18:89]
    s = re.findall('\\b[a-zA-Z]{12,14}\\b', s)
    palindromes = {word for word in set(s) if word.lower() == word[::-1].lower()}
    return palindromes