def sum_in_range(numbers):
    total = 0
    for number in numbers:
        if -100 <= number <= -55:
            total += number
    return total