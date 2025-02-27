import re

def return_n_smallest_chars(s):
    return re.findall('(\\w)', s)[-2]