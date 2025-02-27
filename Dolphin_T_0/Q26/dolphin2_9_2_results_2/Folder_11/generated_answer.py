def sum_in_range(numbers):
    result = 0
    for num in numbers:
        if 11 <= num <= 76:
            result += num
    return result