def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) <= 300:
        return 0
    return integer_list[300] if integer_list[300] % 2 != 0 else 0