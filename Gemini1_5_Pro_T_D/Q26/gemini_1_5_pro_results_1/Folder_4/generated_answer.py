def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 32 and number <= 44:
            sum += number
    return sum