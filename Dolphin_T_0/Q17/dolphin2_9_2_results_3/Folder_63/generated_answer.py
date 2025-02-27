def all_ints_div_by_both_two_nums(ints):
    divisible_by_both = []
    for i in range(31, 51):
        if ints[i] % 81 == 0 and ints[i] % 64 == 0:
            divisible_by_both.append(ints[i])
    return divisible_by_both