def sum_odd_ints_inclusive(numbers):
    odd_sum = 0
    for i in range(min(6, len(numbers))):
        if numbers[i] % 2 != 0:
            odd_sum += numbers[i]
    return odd_sum