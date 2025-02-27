def all_odd_ints_exclusive(int_list):
    odd_ints = [int_ for i, int_ in enumerate(int_list) if i >= 385 and i < 999 and (int_ % 2 != 0)]
    return odd_ints