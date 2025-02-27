def sum_even_ints_inclusive(int_list):
    if len(int_list) < 85:
        return 'Input list is too short. Needs to have at least 85 elements.'
    else:
        return sum((x for x in int_list[69:85] if x % 2 == 0))