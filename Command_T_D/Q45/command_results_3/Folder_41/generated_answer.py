import re

def palindromes_between_indices(str1):
    str1 = str1[2:-3]
    return re.findall('([a-z]+)(?i)([a-z]*)\x01', str1)