def all_ints_div_by_both_two_nums(int_list):
    result = [num for num in int_list[37:82] if num % -61 == 0 and num % -71 == 0]
    return result if result else []