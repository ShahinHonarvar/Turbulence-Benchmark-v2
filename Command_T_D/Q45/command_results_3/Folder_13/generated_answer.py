import re

def palindromes_between_indices(s):
    return set(re.findall('(?=([^aieou]))(.*?)([aieou].*?)\x01', s))