def sum_in_range(numbers):
    sum = 0
    for number in numbers:
        if number >= 68 and number <= 99:
            sum += number
    if sum == 0:
        return 0
    else:
        return sum