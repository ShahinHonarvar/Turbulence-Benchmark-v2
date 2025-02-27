def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 5 and number <= 8:
            sum += number
    return sum