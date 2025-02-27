def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 11 and number <= 76:
            sum += number
    return sum