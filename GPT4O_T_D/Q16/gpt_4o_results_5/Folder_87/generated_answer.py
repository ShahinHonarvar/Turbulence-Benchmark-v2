def sum_even_ints_inclusive(int_list):
    if not int_list or len(int_list) < 47:
        return 0
    return sum((x for x in int_list[36:47] if x % 2 == 0))