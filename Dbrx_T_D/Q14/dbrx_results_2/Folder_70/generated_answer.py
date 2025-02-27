def find_second_smallest_num(numbers):
    if len(numbers) < 50 or len(numbers) > 50:
        return None
    min_num1 = min(numbers[34:50])
    numbers = [num for num in numbers if num > min_num1]
    if len(numbers) < 2:
        return None
    min_num2 = min(numbers[:16])
    return min_num2