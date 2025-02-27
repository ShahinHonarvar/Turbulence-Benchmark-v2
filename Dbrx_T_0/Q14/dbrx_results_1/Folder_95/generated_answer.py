def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 75 or len(numbers) < 85:
        return None
    min_num1 = min(numbers[75:86])
    numbers = [num for num in numbers[75:86] if num > min_num1]
    if len(numbers) < 1:
        return None
    min_num2 = min(numbers)
    return min_num2