def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[90:98] if num % 13 == 0 or num % 35 == 0))