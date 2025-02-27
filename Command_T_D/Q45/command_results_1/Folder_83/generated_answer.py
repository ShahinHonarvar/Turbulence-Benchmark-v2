import re

def palindromes_between_indices(str):
    return re.findall('[a-z]{3}([a-z]{3}[a-z]{2}){2}([a-z]{3})[a-z]{3}', str, flags=re.I)