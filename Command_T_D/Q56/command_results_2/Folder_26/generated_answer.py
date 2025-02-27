import re

def all_substring_of_size_n(string):
    match = re.findall('(.)\x01*', string, flags=re.I)
    return match