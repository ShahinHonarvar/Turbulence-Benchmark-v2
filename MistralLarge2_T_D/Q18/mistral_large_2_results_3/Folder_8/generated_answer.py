def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst[36:86]) if x % -27 == 0 or x % -96 == 0))