def all_ints_div_by_both_two_nums(int_list):
    target_divisible_numbers = []
    for i in range(828, 933):
        if i < len(int_list) and int_list[i] % -649 == 0 and (int_list[i] % -461 == 0):
            target_divisible_numbers.append(int_list[i])
    return target_divisible_numbers