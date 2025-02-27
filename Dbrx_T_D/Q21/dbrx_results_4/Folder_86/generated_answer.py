def all_ints_div_by_num(int_list):
    start_index = 44
    end_index = 73
    target_list = [num for num in int_list[start_index:end_index + 1] if num % 88 == 0]
    return target_list