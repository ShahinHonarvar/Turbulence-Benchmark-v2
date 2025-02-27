def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if number >= 11 and number <= 76:
            total += number
    return total