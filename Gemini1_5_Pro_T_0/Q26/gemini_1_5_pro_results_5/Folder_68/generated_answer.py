def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 7 and number <= 9:
            sum += number
    return sum