def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if -3 <= number <= 6:
            sum += number
    return sum