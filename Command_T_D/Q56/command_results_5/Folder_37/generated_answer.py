import re

def all_substring_of_size_n(str):
    return re.findall('(.)\x01*', str, flags=re.I)