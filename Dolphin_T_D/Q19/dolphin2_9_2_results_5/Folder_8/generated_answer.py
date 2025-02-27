def all_ints_not_div_by_num(num_list):
    desired_nums = [num for num in num_list[17:88] if num % -75 != 0]
    if len(desired_nums) == 0:
        return []
    else:
        return desired_nums