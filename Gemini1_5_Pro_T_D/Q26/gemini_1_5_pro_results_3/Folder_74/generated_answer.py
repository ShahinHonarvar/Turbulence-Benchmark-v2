def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 13 and number <= 35:
            sum += number
    return sum