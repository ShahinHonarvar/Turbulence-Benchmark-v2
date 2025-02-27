def sum_in_range(numbers):
    result = 0
    for num in numbers:
        if num in range(10, 80):
            result += num
    return result