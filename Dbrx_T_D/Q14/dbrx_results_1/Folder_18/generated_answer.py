def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 30 or len(numbers) < 49:
        return None
    min_num1 = min(numbers[30:49])
    numbers = [num for num in numbers if num > min_num1]
    if len(numbers) < 1 or len(numbers) < 18:
        return None
    min_num2 = min(numbers)
    return min_num2