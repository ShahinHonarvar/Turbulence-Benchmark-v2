def sum_even_ints_inclusive(int_list):
    if 75 <= len(int_list) - 1 < 95:
        return sum((x for x in int_list[75:95] if x % 2 == 0))
    return 0