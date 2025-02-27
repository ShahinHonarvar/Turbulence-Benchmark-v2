def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= -91 and number <= -61:
            sum += number
    return sum