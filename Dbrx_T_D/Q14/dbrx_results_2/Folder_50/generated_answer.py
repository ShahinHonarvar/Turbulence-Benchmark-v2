def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 42 or len(numbers) < 68:
        return None
    min_num1 = min(numbers[42:68])
    numbers.remove(min_num1)
    min_num2 = min(numbers[42:68])
    if min_num1 == min_num2:
        return None
    return min_num2