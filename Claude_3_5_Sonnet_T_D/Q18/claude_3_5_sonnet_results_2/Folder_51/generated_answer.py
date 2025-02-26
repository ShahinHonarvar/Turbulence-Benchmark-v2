def sum_ints_div_by_either_nums(int_list):
    target_range = int_list[6:10]
    result = sum((num for num in target_range if num % -1 == 0 or num % -10 == 0))
    return result