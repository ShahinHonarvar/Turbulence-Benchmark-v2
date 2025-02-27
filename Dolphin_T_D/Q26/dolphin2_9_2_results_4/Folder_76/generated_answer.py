def sum_in_range(numbers):
    result = 0
    for number in numbers:
        if 682 <= number <= 744:
            result += number
    if result == 0:
        return 0
    else:
        return result