def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if -8 <= number <= 8:
            sum += number
    return sum