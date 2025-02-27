def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if num in range(32, 45):
            total += num
    return total