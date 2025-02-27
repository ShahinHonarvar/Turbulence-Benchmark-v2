import re

def all_substring_of_size_n(s):
    return re.findall('[a-z]+', s, flags=re.I)