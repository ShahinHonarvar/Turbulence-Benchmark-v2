def sum_in_range(numbers):
    result = 0
    for num in numbers:
        if 3 <= num <= 4:
            result += num
    return result