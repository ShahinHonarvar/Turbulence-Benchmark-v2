def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 60 <= number <= 97:
            total += number
    return total