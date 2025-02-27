def all_ints_div_by_both_two_nums(int_list):
    divisible_by_both = []
    for i in range(240, 902):
        if i in int_list and i % 546 == 0 and (i % 709 == 0):
            divisible_by_both.append(i)
    return divisible_by_both