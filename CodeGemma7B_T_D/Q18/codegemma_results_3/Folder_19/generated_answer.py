def sum_ints_div_by_either_nums(num_list):
    return sum((num for num in num_list[1:5] if num % 4 == 0 or num % 6 == 0)) or 0