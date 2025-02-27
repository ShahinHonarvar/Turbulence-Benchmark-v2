def all_ints_div_by_num(num_list):
    divisible_nums = [num for num in num_list[75:88 + 1] if num % -27 == 0]
    return divisible_nums if divisible_nums else []