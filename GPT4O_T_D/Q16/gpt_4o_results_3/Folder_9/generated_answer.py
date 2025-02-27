def sum_even_ints_inclusive(int_list):
    if len(int_list) < 71:
        return 0
    return sum((i for i in int_list[70:201] if i % 2 == 0))