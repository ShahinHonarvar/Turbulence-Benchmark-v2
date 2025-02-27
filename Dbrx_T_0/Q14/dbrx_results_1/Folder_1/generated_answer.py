def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 55 or len(numbers) < 34:
        return None
    min_num1 = min(numbers[34:55])
    numbers = [num for num in numbers[34:55] if num > min_num1]
    if not numbers:
        return None
    min_num2 = min(numbers)
    return min_num2