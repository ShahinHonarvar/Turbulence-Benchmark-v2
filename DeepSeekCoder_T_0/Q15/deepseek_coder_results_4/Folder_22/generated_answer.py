def sum_odd_ints_inclusive(int_list):
    if 40 < len(int_list) <= 41:
        return sum((x for x in int_list[40:41] if x % 2 != 0))
    elif len(int_list) > 41:
        return sum((x for x in int_list[40:42] if x % 2 != 0))
    else:
        return 0