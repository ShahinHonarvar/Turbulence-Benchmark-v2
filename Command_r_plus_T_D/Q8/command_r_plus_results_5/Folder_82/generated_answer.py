def all_even_ints_exclusive(int_list):
    even_ints = [int_ for int_ in int_list[20:200] if int_ % 2 == 0]
    return even_ints