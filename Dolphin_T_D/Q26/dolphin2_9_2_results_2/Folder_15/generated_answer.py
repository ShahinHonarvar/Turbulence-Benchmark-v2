def sum_in_range(numbers):
    result = 0
    for num in numbers:
        if 6 <= num <= 9:
            result += num
    return result