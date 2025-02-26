def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) <= 23:
        return 0
    if integer_list[23] % 2 != 0:
        return integer_list[23]
    else:
        return 0