def sum_in_range(numbers):
    sum = 0
    for num in numbers:
        if 32 <= num <= 44:
            sum += num
    return sum