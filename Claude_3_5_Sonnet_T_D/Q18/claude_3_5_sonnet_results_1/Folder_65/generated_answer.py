def sum_ints_div_by_either_nums(integers):
    target_range = integers[50:93]
    divisible_ints = [num for num in target_range if num % -94 == 0 or num % -95 == 0]
    return sum(divisible_ints)