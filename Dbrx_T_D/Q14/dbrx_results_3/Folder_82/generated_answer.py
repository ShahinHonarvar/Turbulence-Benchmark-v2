def find_second_smallest_num(numbers):
    if len(numbers) < 202:
        return None
    min_num1 = min(numbers[20:201])
    numbers = [num for num in numbers[20:201] if num > min_num1]
    if not numbers:
        return None
    min_num2 = min(numbers)
    return min_num2 if min_num2 != min_num1 else None