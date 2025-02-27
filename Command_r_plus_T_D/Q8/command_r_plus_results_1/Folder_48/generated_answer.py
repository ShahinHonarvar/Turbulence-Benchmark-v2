def all_even_ints_exclusive(int_list):
    even_ints = [int_ for i, int_ in enumerate(int_list) if i >= 385 and i < 999 and (int_ % 2 == 0)]
    return even_ints