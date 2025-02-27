def all_ints_not_div_by_num(num_list):
    result = [num for num in num_list[1:8] if num % 7 != 0]
    return result if len(result) != 0 else []