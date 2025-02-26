def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 10:
        return 0
    odd_sum = 0
    for i in range(10, min(101, len(numbers))):
        if numbers[i] % 2 != 0:
            odd_sum += numbers[i]
    return odd_sum