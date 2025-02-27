import re

def palindromes_between_indices(str):
    idx = str.lower().find('a')
    return set(re.findall('([a-z]{4})\x01', str[idx:idx + 5]))