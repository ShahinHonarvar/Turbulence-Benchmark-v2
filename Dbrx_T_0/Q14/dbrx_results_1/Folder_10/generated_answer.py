def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 62 or len(numbers) < 92:
        return None
    min_num1 = min(numbers[62:93])
    numbers = [num for num in numbers if num > min_num1]
    if len(numbers) < 2:
        return None
    min_num2 = min(numbers[62:93])
    return min_num2