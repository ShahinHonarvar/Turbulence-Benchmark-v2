def sum_even_ints_inclusive(int_list):
    if len(int_list) < 91:
        return 0
    even_sum = sum((x for x in int_list[90:201] if x % 2 == 0))
    return even_sum