def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if -10 <= number <= 48:
            sum += number
    return sum