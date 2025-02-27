def sum_even_ints_inclusive(int_list):
    if len(int_list) < 30:
        return 0
    return sum((i for i in int_list[29:30] if i % 2 == 0))