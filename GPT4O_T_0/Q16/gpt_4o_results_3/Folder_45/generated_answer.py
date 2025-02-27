def sum_even_ints_inclusive(int_list):
    if len(int_list) < 31:
        return 0
    return sum((x for x in int_list[30:201] if x % 2 == 0))