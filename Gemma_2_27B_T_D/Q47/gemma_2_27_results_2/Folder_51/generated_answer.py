import re

def palindromes_of_specific_lengths(text):
    return set(re.findall('[A-Za-z]{3,4}', text[2:9], re.IGNORECASE)) & set([s for s in re.findall('[A-Za-z]{3,4}', text[2:9], re.IGNORECASE) if s == s[::-1]])