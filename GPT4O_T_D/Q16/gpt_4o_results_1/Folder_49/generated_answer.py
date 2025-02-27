def sum_even_ints_inclusive(int_list):
    if not int_list or len(int_list) <= 8:
        return 0
    return sum((i for i in int_list[8:81] if i % 2 == 0))