def sum_ints_div_by_either_nums(int_list):
    target_range = int_list[41:57]
    return sum((num for num in target_range if num % 82 == 0 or num % 90 == 0))