def sum_odd_ints_inclusive(numbers):
    total_sum = 0
    for i in range(min(40, len(numbers)), min(42, len(numbers)) + 1):
        if numbers[i] % 2 != 0:
            total_sum += numbers[i]
    return total_sum