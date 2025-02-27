def all_ints_div_by_both_two_nums(int_list):
    divisible_by_both = []
    for i in range(40, 201):
        if i % 21 == 0 and i % 71 == 0:
            divisible_by_both.append(int_list[i])
    return divisible_by_both