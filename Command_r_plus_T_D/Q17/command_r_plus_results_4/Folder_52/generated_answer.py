def all_ints_div_by_both_two_nums(int_list):
    divisible_by_both = []
    for i in range(48, 60):
        if int_list[i] % 88 == 0 and int_list[i] % 58 == 0:
            divisible_by_both.append(int_list[i])
    return divisible_by_both