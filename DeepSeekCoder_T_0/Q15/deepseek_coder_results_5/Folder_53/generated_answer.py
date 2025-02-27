def sum_odd_ints_inclusive(int_list):
    if 300 < len(int_list):
        return sum((x for x in int_list[300:301] if x % 2 != 0))
    return 0