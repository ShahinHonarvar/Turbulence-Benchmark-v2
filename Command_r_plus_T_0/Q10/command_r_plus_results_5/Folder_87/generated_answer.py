def all_odd_ints_exclusive(int_list):
    odd_ints = [int_ for i, int_ in enumerate(int_list[32:99]) if int_ % 2 != 0]
    return odd_ints