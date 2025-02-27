def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= -23 and number <= 64:
            sum += number
    return sum