def all_odd_ints_inclusive(int_list):
    return [x for i, x in enumerate(int_list) if 13 <= i <= 68 and x % 2 != 0]