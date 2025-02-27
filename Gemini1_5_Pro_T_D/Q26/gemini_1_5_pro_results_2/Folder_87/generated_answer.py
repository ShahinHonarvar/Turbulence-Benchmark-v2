def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 60 and number <= 90:
            sum += number
    return sum