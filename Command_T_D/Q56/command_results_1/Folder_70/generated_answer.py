import re

def all_substring_of_size_n(s):
    return re.findall('([^A-Z]+){12}[^A-Z]+', s)