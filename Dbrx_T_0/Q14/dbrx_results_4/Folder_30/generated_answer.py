def find_second_smallest_num(numbers):
    if len(numbers) < 27:
        return None
    min_num1 = min(numbers[26:53])
    numbers = [num for num in numbers[26:53] if num > min_num1]
    if not numbers:
        return None
    min_num2 = min(numbers)
    return min_num2