def sum_in_range(numbers):
    result = 0
    for number in numbers:
        if number >= 32 and number <= 44:
            result += number
    return result