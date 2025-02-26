def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 300:
        return 0
    odd_sum = 0
    target_num = numbers[300]
    if target_num % 2 != 0:
        odd_sum += target_num
    return odd_sum