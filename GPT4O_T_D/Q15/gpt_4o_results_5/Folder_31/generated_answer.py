def sum_odd_ints_inclusive(int_list):
    if len(int_list) < 89:
        return 0
    return sum((x for x in int_list[75:89] if x % 2 != 0))