import re

def all_pos_ints_exclusive(x):
    return re.findall('\\d+', x)[60:200]