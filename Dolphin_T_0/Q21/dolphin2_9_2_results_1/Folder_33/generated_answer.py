def all_ints_div_by_num(num_list):
    sub_list = num_list[319:613]
    divisible_nums = [num for num in sub_list if num % -215 == 0]
    return divisible_nums