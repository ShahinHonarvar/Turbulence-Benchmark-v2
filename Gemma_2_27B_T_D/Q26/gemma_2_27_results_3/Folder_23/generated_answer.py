def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if 50 <= number <= 92:
            sum += number
    return sum