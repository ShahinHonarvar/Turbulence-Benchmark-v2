def sum_even_ints_inclusive(int_list):
    even_ints = sum((x for x in int_list[40:42] if x % 2 == 0))
    return even_ints