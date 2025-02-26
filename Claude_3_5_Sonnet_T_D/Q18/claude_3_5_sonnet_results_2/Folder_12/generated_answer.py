def sum_ints_div_by_either_nums(integers):
    target_range = integers[35:65]
    return sum((num for num in target_range if num % -30 == 0 or num % -95 == 0))