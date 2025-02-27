def all_ints_not_div_by_num(num_list):
    not_divisible_list = []
    for i in range(0, 5):
        if num_list[i] % 13 != 0:
            not_divisible_list.append(num_list[i])
    return not_divisible_list