def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if 10 <= number <= 79:
            sum += number
    return sum