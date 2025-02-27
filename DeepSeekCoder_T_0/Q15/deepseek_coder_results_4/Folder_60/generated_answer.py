def sum_odd_ints_inclusive(int_list):
    if 75 <= 85 < len(int_list):
        return sum((x for x in int_list[75:86] if x % 2 != 0))
    return 0