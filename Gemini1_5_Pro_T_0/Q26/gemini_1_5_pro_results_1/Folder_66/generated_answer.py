def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 28 and number <= 96:
            sum += number
    return sum