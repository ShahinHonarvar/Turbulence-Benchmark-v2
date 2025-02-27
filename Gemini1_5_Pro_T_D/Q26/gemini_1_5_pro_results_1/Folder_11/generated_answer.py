def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if 11 <= number <= 76:
            sum += number
    return sum