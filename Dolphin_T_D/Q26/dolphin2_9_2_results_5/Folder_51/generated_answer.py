def sum_in_range(numbers):
    result = 0
    for num in numbers:
        if 2 <= num <= 7:
            result += num
    return result if result else 0