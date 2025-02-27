import re

def all_substring_of_size_n(string):
    return re.findall('[a-z]{1,52}', string)