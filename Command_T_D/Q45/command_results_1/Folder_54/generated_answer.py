import re

def palindromes_between_indices(s):
    return re.findall('(?<=.)\\w{4,9}(?<=.)', s.lower())