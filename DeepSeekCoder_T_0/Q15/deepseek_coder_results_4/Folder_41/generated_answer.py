def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 7:
        return 0
    return sum((x for x in int_list[6:7] if x % 2 != 0))