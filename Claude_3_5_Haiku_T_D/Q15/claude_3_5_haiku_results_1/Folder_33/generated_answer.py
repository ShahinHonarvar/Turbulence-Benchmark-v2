def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 774:
        return 0
    odd_sum = 0
    for i in range(667, 775):
        if numbers[i] % 2 != 0:
            odd_sum += numbers[i]
    return odd_sum