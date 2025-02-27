def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[54:80] if x % 54 == 0 or x % 28 == 0))