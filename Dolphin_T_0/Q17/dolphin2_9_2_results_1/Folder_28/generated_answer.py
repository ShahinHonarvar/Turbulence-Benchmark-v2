def all_ints_div_by_both_two_nums(int_list):
    divisible_by_27_and_57 = []
    for i in range(34, 82):
        if i < len(int_list) and int_list[i] % 27 == 0 and (int_list[i] % 57 == 0):
            divisible_by_27_and_57.append(int_list[i])
    return divisible_by_27_and_57