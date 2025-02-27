def sum_even_ints_inclusive(int_list):
    if 30 <= 200 < len(int_list):
        return sum((x for x in int_list[30:201] if x % 2 == 0))
    return 0