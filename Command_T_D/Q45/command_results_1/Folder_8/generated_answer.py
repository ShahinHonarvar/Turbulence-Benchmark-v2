import re

def palindromes_between_indices(s):
    s = re.sub('[^A-Za-z]+', '', s.lower())
    return set(re.findall('((?=((?=.*?[a-z]))\x01[a-z]+\x01)', s))