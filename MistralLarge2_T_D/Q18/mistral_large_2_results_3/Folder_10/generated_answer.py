def sum_ints_div_by_either_nums(int_list):
    return sum((num for i, num in enumerate(int_list) if 32 <= i <= 99 and (num % -11 == 0 or num % -15 == 0)))