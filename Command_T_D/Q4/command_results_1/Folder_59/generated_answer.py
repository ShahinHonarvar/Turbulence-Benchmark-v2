import re

def all_pos_ints_exclusive(a):
    return re.findall('(?<=\\d)\\d', a)