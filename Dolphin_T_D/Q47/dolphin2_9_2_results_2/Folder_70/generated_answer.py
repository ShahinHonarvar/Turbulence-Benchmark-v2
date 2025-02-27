import re

def palindromes_of_specific_lengths(s):
    substring = s[10:71]
    palindromes = set(re.findall('[a-zA-Z]{24,52}', substring))
    return {p for p in palindromes if p.lower() == p[::-1].lower()}