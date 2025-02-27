def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 87 < 25:
        return None
    min_num1 = min(numbers[25:88])
    numbers = [num for num in numbers[25:88] if num != min_num1]
    if not numbers:
        return None
    min_num2 = min(numbers)
    return min_num2 if min_num2 > min_num1 else None