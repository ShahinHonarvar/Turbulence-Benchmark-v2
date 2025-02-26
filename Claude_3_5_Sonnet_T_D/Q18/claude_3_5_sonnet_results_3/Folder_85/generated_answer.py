def sum_ints_div_by_either_nums(int_list):
    target_range = int_list[1:9]
    divisible_nums = [num for num in target_range if num % -9 == 0 or num % -3 == 0]
    return sum(divisible_nums) if divisible_nums else 0