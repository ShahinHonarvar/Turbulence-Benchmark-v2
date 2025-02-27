def all_ints_div_by_both_two_nums(int_list):
    start_index = 38
    end_index = 81
    return [num for num in int_list[start_index:end_index + 1] if num % -61 == 0 and num % -71 == 0]