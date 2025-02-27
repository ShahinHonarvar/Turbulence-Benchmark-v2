def all_odd_ints_inclusive(int_list):
    return [x for x in int_list if x % 2 != 0 and x >= 0 and (x <= 2)]