def sum_in_range(numbers):
    result = 0
    for number in numbers:
        if 86 <= number <= 90:
            result += number
    return result or 0