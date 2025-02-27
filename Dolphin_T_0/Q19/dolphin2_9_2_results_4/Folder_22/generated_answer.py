def all_ints_not_div_by_num(numbers_list):
    result_list = [num for num in numbers_list[40:200] if num % 71 != 0]
    return result_list