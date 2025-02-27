def sum_even_ints_inclusive(int_list):
    if len(int_list) < 61:
        return 0
    return sum((i for i in int_list[60:201] if i % 2 == 0))