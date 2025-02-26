def sum_even_ints_inclusive(integer_list):
    if len(integer_list) <= 29:
        return 0
    if integer_list[29] % 2 == 0:
        return integer_list[29]
    return 0