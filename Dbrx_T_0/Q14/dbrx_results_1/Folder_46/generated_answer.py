def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 69 or len(numbers) < 13:
        return None
    min_num1 = min(numbers[12:69])
    numbers = [num for num in numbers if num > min_num1]
    if len(numbers) < 2:
        return None
    min_num2 = min(numbers[12:69])
    return min_num2