import re

def all_substring_of_size_n(s):
    return [m.group() for m in re.finditer('([^A-Z0-9]+)', s)]