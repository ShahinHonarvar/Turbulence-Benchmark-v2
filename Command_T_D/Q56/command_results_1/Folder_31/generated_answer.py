import re

def all_substring_of_size_n(s):
    if not s:
        return []
    m = re.fullmatch('(.)\x01*', s)
    if m:
        return [m.group(1)]
    return []