def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if 2 <= number <= 9:
            sum += number
    return sum