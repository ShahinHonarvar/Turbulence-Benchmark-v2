def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 81:
        return None
    min_num1 = min(numbers[40:81])
    numbers = [num for num in numbers[40:81] if num > min_num1]
    if not numbers:
        return None
    min_num2 = min(numbers)
    return min_num2