from functools import reduce

def sum_ints_div_by_either_nums(lst):
    return reduce(lambda x, y: x + y, [i for i in lst[20:94] if i % -92 == 0 or i % -50 == 0], 0)