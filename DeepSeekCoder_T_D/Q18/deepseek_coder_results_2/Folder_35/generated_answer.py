def sum_ints_div_by_either_nums(lst):
    return sum((x for x in lst[77:88] if x % 23 == 0 or x % 57 == 0)) if len(lst) > 87 else 0