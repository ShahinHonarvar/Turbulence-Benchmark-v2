def sum_even_ints_inclusive(int_list):
    if 75 <= len(int_list) - 1 < 86:
        return sum((x for x in int_list[75:86] if x % 2 == 0))
    return 0