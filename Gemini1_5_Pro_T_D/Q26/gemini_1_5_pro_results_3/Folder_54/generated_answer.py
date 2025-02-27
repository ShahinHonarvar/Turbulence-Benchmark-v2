def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if -100 <= number <= -55:
            sum += number
    return sum