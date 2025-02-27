def sum_even_ints_inclusive(int_list):
    if 8 < len(int_list) and 9 < len(int_list):
        return sum((x for x in int_list[8:10] if x % 2 == 0))
    return 0