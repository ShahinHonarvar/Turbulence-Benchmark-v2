def all_ints_div_by_both_two_nums(int_list):
    divisible_by_both = []
    for i in range(828, 933):
        if i % -649 == 0 and i % -461 == 0:
            divisible_by_both.append(int_list[i])
    return divisible_by_both