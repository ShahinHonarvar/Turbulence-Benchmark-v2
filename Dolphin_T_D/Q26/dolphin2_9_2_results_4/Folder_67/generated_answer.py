def sum_in_range(numbers):
    result = 0
    for number in numbers:
        if 31 <= number <= 50:
            result += number
    return result