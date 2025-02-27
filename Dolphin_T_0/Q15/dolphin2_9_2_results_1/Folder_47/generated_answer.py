def sum_odd_ints_inclusive(integer_list):
    return sum((x for i, x in enumerate(integer_list[37:77]) if x % 2 != 0))