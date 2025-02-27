import re

def all_ints_div_by_both_two_nums(lst):
    return [x for x in range(69, 70 + 1) if re.match('(\\d+)%72(\\d+)%70', str(x))]