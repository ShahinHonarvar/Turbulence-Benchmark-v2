import re

def all_substring_of_size_n(str):
    return re.findall('((?:[a-z]){98})', str)