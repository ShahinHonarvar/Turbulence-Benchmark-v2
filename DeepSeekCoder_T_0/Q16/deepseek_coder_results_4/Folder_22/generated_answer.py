def sum_even_ints_inclusive(int_list):
    if 40 < len(int_list) and 41 < len(int_list):
        return sum((x for x in int_list[40:42] if x % 2 == 0))
    return 0