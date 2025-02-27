def sum_odd_ints_inclusive(int_list):
    return sum((x for x in int_list[:6] if x % 2 != 0))