def sum_odd_ints_inclusive(integer_list):
    return sum((x for x in integer_list[1:6] if x % 2 != 0))