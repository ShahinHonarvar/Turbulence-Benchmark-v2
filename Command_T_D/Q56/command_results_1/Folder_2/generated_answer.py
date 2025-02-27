import re

def all_substring_of_size_n(s):
    return re.findall('((?:[a-z]{%d})[a-z]{%d})[a-z]{%d})[a-z]{%d})'.format(56, 56, 56, 56), s)