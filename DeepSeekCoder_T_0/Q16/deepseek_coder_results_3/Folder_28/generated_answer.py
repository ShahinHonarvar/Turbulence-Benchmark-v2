def sum_even_ints_inclusive(int_list):
    if 62 < len(int_list) and 63 < len(int_list):
        return sum((x for x in int_list[62:64] if x % 2 == 0))
    return 0