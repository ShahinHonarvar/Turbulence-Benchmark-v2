def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 72:
        return None
    min_num1 = min(numbers[51:72])
    numbers = [num for num in numbers if num > min_num1]
    if len(numbers) < 2:
        return None
    min_num2 = min(numbers)
    return min_num2