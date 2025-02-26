def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[14:94] if num % 71 == 0 or num % 81 == 0))