def all_ints_div_by_num(int_list):
    target_range = int_list[62:71]
    result = [num for num in target_range if num % 58 == 0]
    return result