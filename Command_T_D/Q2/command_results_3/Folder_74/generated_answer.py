import re

def all_ints_exclusive(lst):
    return [x for x in lst if re.match('^32$', str(x))]