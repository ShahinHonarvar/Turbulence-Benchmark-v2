def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if 4 <= number <= 8:
            sum += number
    return sum