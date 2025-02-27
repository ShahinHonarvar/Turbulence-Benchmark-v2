def find_second_smallest_num(numbers):
    if len(numbers) < 98:
        return None
    min_num1 = min(numbers[20:97])
    numbers = [num for num in numbers if num > min_num1]
    if len(numbers) < 2:
        return None
    min_num2 = min(numbers[20:97])
    return min_num2