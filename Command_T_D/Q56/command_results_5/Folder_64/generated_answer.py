import re

def all_substring_of_size_n(s):
    return re.findall('([a-zA-Z]{1})\x01[a-zA-Z]{6}\x01', s)