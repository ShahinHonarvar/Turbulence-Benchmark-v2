import re

def all_substring_of_size_n(str):
    return re.findall('(?=.)\\w{146}$', str)