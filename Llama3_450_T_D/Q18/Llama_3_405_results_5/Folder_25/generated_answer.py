def sum_ints_div_by_either_nums(num_list):
    return sum((num for i, num in enumerate(num_list) if 25 <= i <= 80 and (num % -20 == 0 or num % -26 == 0)))