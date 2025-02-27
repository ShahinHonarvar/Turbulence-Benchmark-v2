def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 138 <= num <= 858:
            total += num
    return total if total != 0 else 0