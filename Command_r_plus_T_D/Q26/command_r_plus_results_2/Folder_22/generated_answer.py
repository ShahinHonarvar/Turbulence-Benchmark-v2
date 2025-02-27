def sum_in_range(numbers):
    total_sum = 0
    for num in numbers:
        if 4 <= num <= 6:
            total_sum += num
    return total_sum