def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) < 60:
        return None
    min_num1 = min(numbers[60:200])
    numbers = [num for num in numbers[60:200] if num > min_num1]
    if len(numbers) < 1:
        return None
    min_num2 = min(numbers)
    return min_num2