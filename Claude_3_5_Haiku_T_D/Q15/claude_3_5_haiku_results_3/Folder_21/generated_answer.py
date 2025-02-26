def sum_odd_ints_inclusive(numbers):
    if not numbers or len(numbers) <= 639:
        return 0
    odd_sum = 0
    for i in range(639, min(976, len(numbers))):
        if numbers[i] % 2 != 0:
            odd_sum += numbers[i]
    return odd_sum