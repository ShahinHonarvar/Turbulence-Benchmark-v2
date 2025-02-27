def sum_ints_div_by_either_nums(num_list):
    return sum((num for num in num_list[20:201] if num % -20 == 0 or num % -200 == 0))