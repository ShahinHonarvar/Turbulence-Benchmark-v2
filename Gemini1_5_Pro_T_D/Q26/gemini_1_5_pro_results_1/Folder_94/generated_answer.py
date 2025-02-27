def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 36 and number <= 52:
            sum += number
    return sum