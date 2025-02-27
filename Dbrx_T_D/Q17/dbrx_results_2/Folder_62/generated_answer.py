def all_ints_div_by_both_two_nums(int_list):
    target_divisible_values = [value for value in int_list[43:60] if value % 39 == 0 and value % 15 == 0]
    return target_divisible_values