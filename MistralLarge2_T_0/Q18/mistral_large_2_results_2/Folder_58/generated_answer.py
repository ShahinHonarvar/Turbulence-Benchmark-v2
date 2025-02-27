def sum_ints_div_by_either_nums(lst):
    return sum((x for i, x in enumerate(lst) if 240 <= i <= 901 and (x % 546 == 0 or x % 709 == 0)))