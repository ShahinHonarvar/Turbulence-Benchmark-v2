def sum_in_range(numbers):
    result = 0
    for number in numbers:
        if number >= 18 and number <= 52:
            result += number
    return result