def sum_even_ints_inclusive(int_list):
    if 27 >= len(int_list) or 55 >= len(int_list):
        return 0
    return sum((x for x in int_list[27:56] if x % 2 == 0))