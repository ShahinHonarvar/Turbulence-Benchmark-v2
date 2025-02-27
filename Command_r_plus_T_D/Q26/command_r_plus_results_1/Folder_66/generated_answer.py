def sum_in_range(numbers):
    total_sum = 0
    for num in numbers:
        if 28 <= num <= 96:
            total_sum += num
    return total_sum