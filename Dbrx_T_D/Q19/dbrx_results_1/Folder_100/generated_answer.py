def all_ints_not_div_by_num(integer_list):
    start_index = 62
    end_index = 96
    nums = [num for num in integer_list[start_index:end_index] if num % 26 != 0]
    return nums