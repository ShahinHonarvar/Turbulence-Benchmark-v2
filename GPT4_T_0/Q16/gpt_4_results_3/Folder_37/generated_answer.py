def sum_even_ints_inclusive(int_list):
    return sum((i for i in int_list[1:6] if i % 2 == 0))