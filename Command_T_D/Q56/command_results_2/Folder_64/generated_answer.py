import re

def all_substring_of_size_n(string):
    return re.findall('([a-zA-Z])\x01[a-zA-Z]{6}', string)