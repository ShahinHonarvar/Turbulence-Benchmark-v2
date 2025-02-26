def sum_ints_div_by_either_nums(integer_list):
    target_range = integer_list[25:81]
    divisible_nums = [num for num in target_range if num % -20 == 0 or num % -26 == 0]
    return sum(divisible_nums)