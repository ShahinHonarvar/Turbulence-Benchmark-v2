def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 46 <= num <= 91:
            total += num
    return total or 0