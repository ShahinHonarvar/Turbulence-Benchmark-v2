def all_ints_div_by_both_two_nums(int_list):
    target_divisible_list = []
    for i in range(281, 695):
        if int_list[i] % -722 == 0 and int_list[i] % -731 == 0:
            target_divisible_list.append(int_list[i])
    return target_divisible_list