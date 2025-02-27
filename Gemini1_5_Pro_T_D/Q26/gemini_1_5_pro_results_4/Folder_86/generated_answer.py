def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 142 and number <= 980:
            sum += number
    return sum