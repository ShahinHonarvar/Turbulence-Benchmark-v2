def all_odd_ints_exclusive(int_list):
    return [x for i, x in enumerate(int_list) if 0 < i < 2 and x % 2 != 0]