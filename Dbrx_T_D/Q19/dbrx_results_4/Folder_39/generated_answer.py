def all_ints_not_div_by_num(input_list):
    not_divisible = [num for num in input_list[22:97] if num % -46 != 0]
    return not_divisible