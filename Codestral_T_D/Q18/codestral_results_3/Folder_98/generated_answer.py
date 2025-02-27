def sum_ints_div_by_either_nums(num_list):
    return sum((num for num in num_list[0:6] if num % -1 == 0 or num % 13 == 0))