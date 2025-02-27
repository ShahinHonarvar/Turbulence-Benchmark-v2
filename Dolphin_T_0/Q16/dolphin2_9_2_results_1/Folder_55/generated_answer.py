def sum_even_ints_inclusive(if_list):
    return sum((i for i in if_list[:11] if i % 2 == 0))