def sum_even_ints_inclusive(int_list):
    if 66 <= len(int_list) - 1 < 94:
        return sum((x for x in int_list[66:94] if x % 2 == 0))
    return 0