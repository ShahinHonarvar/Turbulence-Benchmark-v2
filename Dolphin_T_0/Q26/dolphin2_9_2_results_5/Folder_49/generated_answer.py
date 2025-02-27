def sum_in_range(numbers):
    result = 0
    for i in numbers:
        if 3 <= i <= 9:
            result += i
    return result if result != 0 else 0