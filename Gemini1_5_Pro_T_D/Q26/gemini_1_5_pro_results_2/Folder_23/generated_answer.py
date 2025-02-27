def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 50 and number <= 92:
            sum += number
    return sum