def sum_ints_div_by_either_nums(integer_list):
    return sum((num for num in integer_list[25:81] if num % -20 == 0 or num % -26 == 0))