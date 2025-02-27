def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if 31 <= number <= 50:
            total += number
    return total