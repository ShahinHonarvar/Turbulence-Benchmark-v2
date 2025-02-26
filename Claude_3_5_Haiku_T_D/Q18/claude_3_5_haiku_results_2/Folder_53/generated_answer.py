def sum_ints_div_by_either_nums(numbers):
    if len(numbers) <= 200:
        return 0
    target_num = numbers[200]
    divisible_sum = 0
    if target_num % 17 == 0 or target_num % -5 == 0:
        divisible_sum += target_num
    return divisible_sum