import re

def palindromes_between_indices(str):
    return re.findall('[a-z]+[a-z]{2}|[a-z]{2}[a-z]+', str[3:-7])