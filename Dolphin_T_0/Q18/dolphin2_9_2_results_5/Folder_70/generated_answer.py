def sum_ints_div_by_either_nums(ints):
    total = 0
    for integer in ints[42:44]:
        if integer % 15 == 0 or integer % 87 == 0:
            total += integer
    return total