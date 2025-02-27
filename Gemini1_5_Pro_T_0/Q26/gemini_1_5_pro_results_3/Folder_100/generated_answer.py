def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 19 and number <= 32:
            sum += number
    return sum