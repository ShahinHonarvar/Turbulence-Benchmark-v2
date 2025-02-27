def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 201:
        return None
    min_num1 = min(numbers[20:200])
    numbers = [num for num in numbers[20:200] if num > min_num1]
    if not numbers:
        return None
    min_num2 = min(numbers)
    return min_num2