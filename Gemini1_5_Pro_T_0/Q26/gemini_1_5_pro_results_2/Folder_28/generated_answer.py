def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 10 and number <= 97:
            sum += number
    return sum