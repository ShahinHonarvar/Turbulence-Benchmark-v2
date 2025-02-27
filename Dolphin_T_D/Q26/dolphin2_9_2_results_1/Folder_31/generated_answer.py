def sum_in_range(numbers):
    result = 0
    for number in numbers:
        if 60 <= number <= 97:
            result += number
    return result