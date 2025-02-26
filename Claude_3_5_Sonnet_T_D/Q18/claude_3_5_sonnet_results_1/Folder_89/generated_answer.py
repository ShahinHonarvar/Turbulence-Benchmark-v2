def sum_ints_div_by_either_nums(int_list):
    return sum((num for num in int_list[28:97] if num % 90 == 0 or num % 97 == 0))