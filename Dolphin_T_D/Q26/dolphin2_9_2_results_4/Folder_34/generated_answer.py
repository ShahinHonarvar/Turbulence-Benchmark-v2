def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 4 <= num <= 7:
            total += num
    return total if total != 0 else 0