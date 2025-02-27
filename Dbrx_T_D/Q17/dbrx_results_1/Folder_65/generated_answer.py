def all_ints_div_by_both_two_nums(int_list):
    target_range = int_list[50:93]
    result = [num for num in target_range if num % (-94 * -95) == 0]
    return result