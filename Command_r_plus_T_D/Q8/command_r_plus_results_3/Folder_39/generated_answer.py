def all_even_ints_exclusive(int_list):
    return [int_ for i, int_ in enumerate(int_list) if i >= 43 and i < 99 and (int_ % 2 == 0)]