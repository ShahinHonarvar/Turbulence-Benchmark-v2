def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[40:201] if num % 21 == 0 or num % 71 == 0))