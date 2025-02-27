def sum_in_range(numbers):
    result = 0
    for num in numbers:
        if num >= 3 and num <= 6:
            result += num
    return result if result != 0 else None