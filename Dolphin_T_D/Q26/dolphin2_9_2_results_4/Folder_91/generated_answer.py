def sum_in_range(numbers):
    result = 0
    for number in numbers:
        if -8 <= number <= 8:
            result += number
    return result