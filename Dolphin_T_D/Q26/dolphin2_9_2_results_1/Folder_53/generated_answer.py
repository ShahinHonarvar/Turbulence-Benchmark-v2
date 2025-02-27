def sum_in_range(numbers):
    result = 0
    for number in numbers:
        if 5 <= number <= 7:
            result += number
    return result