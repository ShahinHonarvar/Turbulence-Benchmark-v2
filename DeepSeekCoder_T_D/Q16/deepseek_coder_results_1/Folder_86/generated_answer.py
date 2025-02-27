def sum_even_ints_inclusive(int_list):
    if 31 <= len(int_list) - 1 < 35:
        return sum((x for x in int_list[31:35] if x % 2 == 0))
    return 0