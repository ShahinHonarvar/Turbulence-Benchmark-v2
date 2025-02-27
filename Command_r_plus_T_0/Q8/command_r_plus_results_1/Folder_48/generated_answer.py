def all_even_ints_exclusive(int_list):
    even_ints = [int_ for i, int_ in enumerate(int_list[385:999]) if int_ % 2 == 0]
    return even_ints