def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 18 and number <= 60:
            sum += number
    return sum