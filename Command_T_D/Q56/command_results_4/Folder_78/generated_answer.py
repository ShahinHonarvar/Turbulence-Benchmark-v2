import re

def all_substring_of_size_n(string):
    pattern = '[A-Z]{%d}' % 49
    matches = re.findall(pattern, string)
    return list(set(matches))