def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= -64 and number <= 42:
            sum += number
    return sum