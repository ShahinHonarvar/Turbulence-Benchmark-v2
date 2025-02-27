def all_even_ints_exclusive(int_list):
    even_ints = [int_ for i, int_ in enumerate(int_list) if int_ % 2 == 0 and 323 <= i < 972]
    return even_ints