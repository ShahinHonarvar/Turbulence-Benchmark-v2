def all_even_ints_inclusive(int_list):
    return [int_ for i, int_ in enumerate(int_list) if i >= 29 and i <= 79 and (int_ % 2 == 0)]