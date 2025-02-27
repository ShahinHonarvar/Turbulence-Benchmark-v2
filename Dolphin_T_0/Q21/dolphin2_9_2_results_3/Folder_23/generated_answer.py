def all_ints_div_by_num(int_list):
    divisible_nums = [num for num in int_list[59:98] if num % -36 == 0]
    return divisible_nums if divisible_nums else []