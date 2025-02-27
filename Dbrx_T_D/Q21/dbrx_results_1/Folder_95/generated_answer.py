def all_ints_div_by_num(integer_list):
    target_range = integer_list[74:86]
    return [num for num in target_range if num % -40 == 0]