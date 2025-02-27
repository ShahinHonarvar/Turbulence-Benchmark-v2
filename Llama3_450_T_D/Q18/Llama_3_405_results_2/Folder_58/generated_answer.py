def sum_ints_div_by_either_nums(lst):
    return sum((i for idx, i in enumerate(lst) if 240 <= idx <= 901 and (i % 546 == 0 or i % 709 == 0)))