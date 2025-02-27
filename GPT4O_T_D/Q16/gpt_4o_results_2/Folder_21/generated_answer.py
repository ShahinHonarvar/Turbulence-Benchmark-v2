def sum_even_ints_inclusive(int_list):
    if len(int_list) < 976:
        return 0
    return sum((n for n in int_list[639:976] if n % 2 == 0))