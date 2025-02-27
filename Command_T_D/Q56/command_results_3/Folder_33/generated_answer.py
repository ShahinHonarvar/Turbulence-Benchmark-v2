import re

def all_substring_of_size_n(str):
    if len(str) < 105:
        return []
    else:
        return re.findall('(.)\x01*', str)