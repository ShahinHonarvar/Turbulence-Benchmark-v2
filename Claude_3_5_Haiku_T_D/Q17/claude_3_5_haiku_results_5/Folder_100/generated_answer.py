def all_ints_div_by_both_two_nums(input_list):
    result = [num for num in input_list[72:94] if num % 32 == 0 and num % 44 == 0]
    return result