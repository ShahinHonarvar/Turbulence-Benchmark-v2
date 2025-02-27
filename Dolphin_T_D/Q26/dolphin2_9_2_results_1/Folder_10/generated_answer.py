def sum_in_range(numbers):
    total = 0
    for num in numbers:
        if 73 <= num <= 84:
            total += num
    if total == 0:
        return 0
    else:
        return total