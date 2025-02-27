import re

def all_substring_of_size_n(s):
    if len(s) < 56:
        return []
    return re.findall('[a-z]{56}', s)