def sum_even_ints_inclusive(int_list):
    if len(int_list) < 7:
        return 0
    even_sum = sum((i for i in int_list[6:7] if i % 2 == 0))
    return even_sum