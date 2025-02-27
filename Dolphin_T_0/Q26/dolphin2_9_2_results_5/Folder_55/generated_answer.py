def sum_in_range(numbers):
    sum = 0
    for num in numbers:
        if 3 <= num <= 6:
            sum += num
    return sum