def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 34 <= number <= 69:
            total += number
    if total == 0:
        return 0
    else:
        return total