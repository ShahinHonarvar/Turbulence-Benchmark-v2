def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 20:
        return 0
    return sum((x for x in int_list[19:93] if x % 2 != 0))