def sum_even_ints_inclusive(int_list):
    if len(int_list) < 65:
        return 'Input list should have at least 65 elements'
    else:
        return sum((x for x in int_list[14:65] if x % 2 == 0))