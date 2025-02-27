def find_second_largest_num(numbers):
    if 23 < len(numbers):
        numbers = numbers[23:24]
        if len(numbers) > 1:
            numbers.sort()
            return numbers[1]
    return None