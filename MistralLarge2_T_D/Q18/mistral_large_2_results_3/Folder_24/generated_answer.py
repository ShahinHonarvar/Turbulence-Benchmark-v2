def sum_ints_div_by_either_nums(int_list):
    return sum((num for idx, num in enumerate(int_list) if 29 <= idx <= 53 and (num % -68 == 0 or num % -85 == 0)))