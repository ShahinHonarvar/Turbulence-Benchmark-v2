import re

def all_substring_of_size_n(s):
    return re.findall('[A-Z][A-Z][A-Z]', s)