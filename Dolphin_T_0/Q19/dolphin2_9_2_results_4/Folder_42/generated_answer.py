def all_ints_not_div_by_num(num_list):
    result = [num for num in num_list[11:56] if num % 90 != 0]
    return result if result else []