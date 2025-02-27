def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 36 <= num <= 52:
            total += num
    if total == 0:
        return 0
    else:
        return total