def sum_odd_ints_inclusive(numbers):
    if len(numbers) < 6:
        return 0
    odd_sum = 0
    for i in range(1, 6):
        if numbers[i] % 2 != 0:
            odd_sum += numbers[i]
    return odd_sum