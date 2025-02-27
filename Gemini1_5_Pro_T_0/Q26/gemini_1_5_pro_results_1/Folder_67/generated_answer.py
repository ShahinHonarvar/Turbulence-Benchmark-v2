def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 31 and number <= 50:
            sum += number
    return sum