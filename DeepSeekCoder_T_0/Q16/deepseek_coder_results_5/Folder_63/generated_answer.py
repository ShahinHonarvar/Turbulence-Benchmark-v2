def sum_even_ints_inclusive(int_list):
    if 22 > len(int_list) - 1 or 88 > len(int_list) - 1:
        return 0
    return sum((x for x in int_list[22:89] if x % 2 == 0))