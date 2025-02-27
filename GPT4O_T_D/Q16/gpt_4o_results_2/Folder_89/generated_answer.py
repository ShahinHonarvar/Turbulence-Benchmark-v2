def sum_even_ints_inclusive(int_list):
    if len(int_list) < 83:
        return 0
    return sum((i for i in int_list[56:83] if i % 2 == 0))