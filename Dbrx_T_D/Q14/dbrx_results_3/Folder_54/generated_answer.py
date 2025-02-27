def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 86 - 68 + 1:
        return None
    min_num1 = min(numbers[68:87])
    numbers = [num for num in numbers[68:87] if num > min_num1]
    if len(numbers) == 0:
        return None
    return min(numbers)