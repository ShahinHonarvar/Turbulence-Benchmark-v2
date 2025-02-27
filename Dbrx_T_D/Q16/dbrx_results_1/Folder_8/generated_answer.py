def sum_even_ints_inclusive(int_list):
    if len(int_list) < 23 or not all((isinstance(i, int) for i in int_list[23:24])):
        return 0
    return sum((x for x in int_list[23:24] if x % 2 == 0))