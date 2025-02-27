def all_even_ints_inclusive(int_list):
    return [int_ for i, int_ in enumerate(int_list) if i >= 25 and i <= 59 and (int_ % 2 == 0)]