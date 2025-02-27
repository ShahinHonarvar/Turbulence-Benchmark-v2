import re

def all_substring_of_size_n(s):
    return [m.group() for m in re.finditer('(?=.)(.)\x01\x02\x03\x04\x05\x06\x07\\8\\9', s)]