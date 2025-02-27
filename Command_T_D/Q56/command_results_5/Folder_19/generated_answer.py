import re

def all_substring_of_size_n(string):
    match = re.findall('(.)\x01*', string)
    if len(match) == 0:
        return []
    return [m for m in match if len(m) == 18]