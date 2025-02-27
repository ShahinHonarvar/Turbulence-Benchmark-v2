def sum_ints_div_by_either_nums(int_list):
    return sum((num for i, num in enumerate(int_list) if 25 <= i <= 70 and (num % 74 == 0 or num % 15 == 0)))