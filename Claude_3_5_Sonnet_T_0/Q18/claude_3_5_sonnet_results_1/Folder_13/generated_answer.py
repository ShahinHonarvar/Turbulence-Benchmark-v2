def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[13:19] if num % 45 == 0 or num % 20 == 0))