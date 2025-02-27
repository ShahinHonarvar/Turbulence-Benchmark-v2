def sum_in_range(numbers):
    sum = 0
    for num in numbers:
        if 4 <= num <= 8:
            sum += num
    return sum