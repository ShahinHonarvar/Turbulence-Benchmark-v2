def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 22:
        return 0
    odd_sum = 0
    for i in range(22, min(51, len(numbers))):
        if numbers[i] % 2 != 0:
            odd_sum += numbers[i]
    return odd_sum