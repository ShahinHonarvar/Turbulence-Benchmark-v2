def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if 18 <= number <= 60:
            sum += number
    return sum