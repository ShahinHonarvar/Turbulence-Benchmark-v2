def sum_in_range(numbers):
    result = 0
    for num in numbers:
        if 3 <= num <= 8:
            result += num
    return result if result != 0 else 0