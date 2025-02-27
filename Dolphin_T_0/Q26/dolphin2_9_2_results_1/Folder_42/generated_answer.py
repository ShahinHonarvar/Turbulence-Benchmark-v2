def sum_in_range(numbers):
    result = 0
    for num in numbers:
        if num in range(141, 263):
            result += num
    return result