import re

def all_substring_of_size_n(s):
    return re.findall('(\\S){73}(\\S)', s)