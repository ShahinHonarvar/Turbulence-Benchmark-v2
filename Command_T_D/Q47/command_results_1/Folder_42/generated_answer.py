import re

def palindromes_of_specific_lengths(str):
    return set(re.findall('(?<=.)(.)\\1', str[43:95], flags=re.I))