import re

def all_substring_of_size_n(s):
    return re.findall('([\\d\\w]+){0,73}', s)