def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if 36 <= number <= 52:
            sum += number
    return sum