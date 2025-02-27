def sum_in_range(numbers):
    sum = 0
    for x in numbers:
        if x >= 32 and x <= 44:
            sum += x
    return sum