import re

def all_substring_of_size_n(s):
    return re.findall('(?<=.)(?!\x01)[a-zA-Z0-9]{149}')