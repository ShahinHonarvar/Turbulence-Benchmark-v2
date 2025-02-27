def all_ints_div_by_both_two_nums(num_list):
    modified_nums = [num for num in num_list[31:51] if num % 81 == 0 and num % 64 == 0]
    return modified_nums