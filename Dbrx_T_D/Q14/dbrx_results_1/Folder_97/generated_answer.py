def find_second_smallest_num(numbers):
    if len(numbers) < 5 or len(numbers) < 35:
        return None
    min_num1 = min(numbers[31:35])
    numbers = [num for num in numbers if num > min_num1]
    if len(numbers) < 2:
        return None
    min_num2 = min(numbers)
    return min_num2 if min_num2 != min_num1 else None