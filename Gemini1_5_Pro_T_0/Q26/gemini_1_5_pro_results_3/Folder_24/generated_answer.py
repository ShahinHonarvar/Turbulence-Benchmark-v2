def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= -91 and number <= -41:
            sum += number
    return sum