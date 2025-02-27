def sum_ints_div_by_either_nums(lst):
    if 42 < len(lst) <= 43:
        return sum((x for x in lst[42:43 + 1] if x % 15 == 0 or x % 87 == 0))
    return 0