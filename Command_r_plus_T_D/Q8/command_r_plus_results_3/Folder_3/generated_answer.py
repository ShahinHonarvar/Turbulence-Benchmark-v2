def all_even_ints_exclusive(int_list):
    return [int_ for i, int_ in enumerate(int_list) if i >= 78 and i < 93 and (int_ % 2 == 0)]