import re

def all_substring_of_size_n(str1):
    return re.findall('[a-z]+', str1, flags=re.I)