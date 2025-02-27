import re

def all_substring_of_size_n(s):
    return [m.group() for m in re.finditer('<{}.>'.format(49), s)]