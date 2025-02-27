def sum_odd_ints_inclusive(int_list):
    odds = sum((x for x in int_list[34:50] if x % 2 != 0))
    return odds if odds != 0 else 0