def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 3 and number <= 4:
            sum += number
    return sum