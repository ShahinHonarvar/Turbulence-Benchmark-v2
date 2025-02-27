def all_ints_div_by_both_two_nums(num_list):
    start_index = 46
    end_index = 91
    result = [num for num in num_list[start_index:end_index + 1] if num % 67 == 0 and num % 15 == 0]
    return result