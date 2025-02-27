def find_second_smallest_num(numbers):
    if len(numbers) < 5 or len(numbers) < 33:
        return None
    min_num1 = min(numbers[28:33])
    numbers = [num for num in numbers[28:33] if num > min_num1]
    if len(numbers) < 2:
        return None
    min_num2 = min(numbers)
    return min_num2