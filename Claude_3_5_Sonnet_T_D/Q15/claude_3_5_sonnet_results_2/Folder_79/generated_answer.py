def sum_odd_ints_inclusive(integer_list):
    if len(integer_list) >= 5:
        return integer_list[4] if integer_list[4] % 2 != 0 else 0
    else:
        return 0