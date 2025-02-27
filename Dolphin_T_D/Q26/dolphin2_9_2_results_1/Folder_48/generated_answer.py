def sum_in_range(numbers):
    result = 0
    for number in numbers:
        if 827 <= number <= 999:
            result += number
    return result if result > 0 else 0