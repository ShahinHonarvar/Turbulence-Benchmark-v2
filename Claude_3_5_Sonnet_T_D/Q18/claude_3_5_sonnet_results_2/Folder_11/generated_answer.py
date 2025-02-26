def sum_ints_div_by_either_nums(numbers):
    target_range = numbers[22:25]
    sum_divisible = sum((num for num in target_range if num % -85 == 0 or num % -30 == 0))
    return sum_divisible