def all_odd_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if i > 3 and i < 8 and (x % 2 != 0)]