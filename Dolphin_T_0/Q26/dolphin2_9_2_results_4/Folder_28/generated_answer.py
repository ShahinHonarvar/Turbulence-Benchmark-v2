def sum_in_range(numbers):
    result = 0
    for number in numbers:
        if number >= 10 and number <= 97:
            result += number
    return result