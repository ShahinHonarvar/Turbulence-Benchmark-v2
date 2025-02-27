def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 50:
        return None
    min_num1 = min(numbers[35:50])
    numbers = [num for num in numbers[35:50] if num > min_num1]
    if not numbers:
        return None
    min_num2 = min(numbers)
    return min_num2