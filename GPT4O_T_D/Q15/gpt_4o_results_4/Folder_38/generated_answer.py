def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 64:
        return 0
    return sum((x for x in int_list[22:64] if x % 2 != 0))