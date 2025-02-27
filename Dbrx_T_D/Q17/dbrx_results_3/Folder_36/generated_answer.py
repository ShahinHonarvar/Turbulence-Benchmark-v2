def all_ints_div_by_both_two_nums(integer_list):
    target_range = integer_list[299:383]
    return [num for num in target_range if num % 858 == 0 and num % 952 == 0]