def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 52 or len(numbers) - 29 < 2:
        return None
    min_num1 = min(numbers[29:52])
    numbers = [num for num in numbers[29:52] if num > min_num1]
    min_num2 = min(numbers) if numbers else None
    return min_num2