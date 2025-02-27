def sum_even_ints_inclusive(int_list):
    if len(int_list) < 51:
        return 0
    even_sum = sum((i for i in int_list[50:201] if i % 2 == 0))
    return even_sum