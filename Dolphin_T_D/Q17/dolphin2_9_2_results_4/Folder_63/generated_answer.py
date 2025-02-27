def all_ints_div_by_both_two_nums(ints):
    return [ints[i] for i in range(31, 51) if ints[i] % 81 == 0 and ints[i] % 64 == 0]