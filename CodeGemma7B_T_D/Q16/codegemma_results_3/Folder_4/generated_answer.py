def sum_even_ints_inclusive(int_list):
    if not any((i % 2 == 0 for i in int_list[12:93])):
        return 0
    return sum((i for i in int_list[12:93] if i % 2 == 0))