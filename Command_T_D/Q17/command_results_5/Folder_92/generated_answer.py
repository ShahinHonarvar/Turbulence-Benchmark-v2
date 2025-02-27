import re

def all_ints_div_by_both_two_nums(lst):
    if not lst:
        return []
    return [int(x) for x in re.findall('([+-]?)\\d+', str(lst))]