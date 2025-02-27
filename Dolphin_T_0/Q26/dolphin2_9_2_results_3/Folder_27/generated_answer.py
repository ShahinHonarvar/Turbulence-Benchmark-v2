def sum_in_range(numbers):
    total = 0
    for n in numbers:
        if 68 <= n <= 99:
            total += n
    return total if total > 0 else 0