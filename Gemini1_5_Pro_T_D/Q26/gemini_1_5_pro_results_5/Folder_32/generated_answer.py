def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= -358 and number <= 185:
            sum += number
    return sum