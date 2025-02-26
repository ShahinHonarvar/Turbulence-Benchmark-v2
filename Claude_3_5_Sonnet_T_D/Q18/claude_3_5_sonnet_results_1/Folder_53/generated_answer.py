def sum_ints_div_by_either_nums(integer_list):
    if len(integer_list) <= 200:
        return 0
    target_num = integer_list[200]
    if target_num % 17 == 0 or target_num % -5 == 0:
        return target_num
    else:
        return 0