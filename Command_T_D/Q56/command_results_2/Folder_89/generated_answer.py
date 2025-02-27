import re

def all_substring_of_size_n(str):
    return [m.group() for m in re.finditer('(.)\x01*', str, flags=re.I)]