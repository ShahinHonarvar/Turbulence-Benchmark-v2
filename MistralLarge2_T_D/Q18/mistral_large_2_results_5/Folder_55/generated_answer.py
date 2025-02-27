def sum_ints_div_by_either_nums(int_list):
    return sum((num for i, num in enumerate(int_list[:10]) if num % 10 == 0 or num % 100 == 0))