def sum_even_ints_inclusive(int_list):
    if 56 < len(int_list) and 57 < len(int_list):
        return sum((x for x in int_list[56:58] if x % 2 == 0))
    return 0