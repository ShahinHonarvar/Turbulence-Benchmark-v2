import re

def all_substring_of_size_n(s):
    m = re.findall('([a-z]){28}', s)
    return m