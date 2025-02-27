def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 13 <= number <= 35:
            total += number
    return total