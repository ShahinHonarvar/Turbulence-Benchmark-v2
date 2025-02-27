import re

def all_pos_ints_exclusive(lst):
    s = str(lst)
    return re.findall('(?<![0-9])[0-9]+', s)[10:-6]