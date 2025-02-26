def sum_odd_ints_inclusive(numbers):
    if len(numbers) <= 98:
        return 0
    odd_sum = 0
    for i in range(55, 99):
        if numbers[i] % 2 != 0:
            odd_sum += numbers[i]
    return odd_sum