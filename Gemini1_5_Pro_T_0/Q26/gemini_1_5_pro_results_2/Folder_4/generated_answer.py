def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if 32 <= number <= 44:
            sum += number
    return sum