def sum_ints_div_by_either_nums(num_list):
    return sum((num for num in num_list[81:90] if num % 56 == 0 or num % 68 == 0))