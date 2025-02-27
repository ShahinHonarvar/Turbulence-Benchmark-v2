def sum_in_range(numbers):
    sum = 0
    for num in numbers:
        if num >= 18 and num <= 52:
            sum += num
    return sum