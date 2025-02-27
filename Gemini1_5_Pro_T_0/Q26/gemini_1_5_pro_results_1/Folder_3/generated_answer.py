def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 38 and number <= 81:
            sum += number
    return sum