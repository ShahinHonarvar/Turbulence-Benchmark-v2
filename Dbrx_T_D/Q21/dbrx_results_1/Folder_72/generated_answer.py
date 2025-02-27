def all_ints_div_by_num(num_list):
    target_range = num_list[11:83]
    result = [num for num in target_range if num % -47 == 0]
    return result