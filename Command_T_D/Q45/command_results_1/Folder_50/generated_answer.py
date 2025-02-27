import re

def palindromes_between_indices(str):
    return set(re.findall('(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[A-Z])\x01\x02\x03\x04\x05\x06\x07\\8\x01\x02\x03\x04\x05\x06\x07\\8', str.lower()))