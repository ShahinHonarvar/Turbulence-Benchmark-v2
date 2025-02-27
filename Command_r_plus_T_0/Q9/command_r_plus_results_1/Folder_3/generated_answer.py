def all_odd_ints_inclusive(int_list):
    return [int_ for i, int_ in enumerate(int_list) if i >= 62 and i <= 92 and (int_ % 2 != 0)]