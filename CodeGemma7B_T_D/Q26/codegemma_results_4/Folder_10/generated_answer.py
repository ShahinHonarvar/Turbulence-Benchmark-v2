def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number in range(73, 85):
            sum += number
    return sum