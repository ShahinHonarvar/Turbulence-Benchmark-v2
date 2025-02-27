import re

def palindromes_between_indices(s):
    reg = '(?i)(?=([a-z])[a-z]{4}([a-z]))([a-z]{4})([a-z]?)\x01([a-z]?)\x02([a-z]{4})\x03([a-z]?)\x04([a-z]?)\x05([a-z]?)\x06([a-z]?)\x07([a-z]?)\\8([a-z]?)\\9([a-z]?)'
    return re.findall(reg, s, flags=re.I)