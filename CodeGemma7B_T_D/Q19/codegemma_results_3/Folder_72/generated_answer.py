def all_ints_not_div_by_num(int_list):
    result = [num for num in int_list[13:70] if num % -78 != 0]
    return result if result else []