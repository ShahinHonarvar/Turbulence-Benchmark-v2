def sum_even_ints_inclusive(int_list):
    if len(int_list) > 111:
        target_index = 111
        if int_list[target_index] % 2 == 0:
            return int_list[target_index]
    return 0