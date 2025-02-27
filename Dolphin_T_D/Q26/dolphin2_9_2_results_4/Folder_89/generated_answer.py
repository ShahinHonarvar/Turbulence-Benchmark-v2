def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 15 <= num <= 57:
            total += num
    return total if total != 0 else None