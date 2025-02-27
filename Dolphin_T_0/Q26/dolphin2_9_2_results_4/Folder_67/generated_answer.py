def sum_in_range(numbers):
    sum = 0
    for num in numbers:
        if 31 <= num <= 50:
            sum += num
    return sum