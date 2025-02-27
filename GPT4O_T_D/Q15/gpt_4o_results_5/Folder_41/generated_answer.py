def sum_odd_ints_inclusive(int_list):
    if len(int_list) > 6:
        target_number = int_list[6]
        if target_number % 2 != 0:
            return target_number
    return 0