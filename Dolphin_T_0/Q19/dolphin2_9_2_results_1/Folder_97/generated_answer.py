def all_ints_not_div_by_num(num_list):
    result = [num for num in num_list[14:48] if num % 16 != 0]
    return result