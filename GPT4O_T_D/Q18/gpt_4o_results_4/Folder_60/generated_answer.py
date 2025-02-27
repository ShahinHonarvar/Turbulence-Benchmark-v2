def sum_ints_div_by_either_nums(lst):
    if len(lst) < 80:
        lst = lst + [0] * (80 - len(lst))
    return sum((x for x in lst[10:80] if x % -74 == 0 or x % -58 == 0))