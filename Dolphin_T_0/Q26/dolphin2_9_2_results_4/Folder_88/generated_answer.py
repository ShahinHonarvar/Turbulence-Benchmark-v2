def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 1 <= number <= 7:
            total += number
    return total