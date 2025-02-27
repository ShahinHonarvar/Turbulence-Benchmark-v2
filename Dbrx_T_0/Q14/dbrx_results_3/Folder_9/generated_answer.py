def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 200 or len(numbers) < 70:
        return None
    min_num1 = min(numbers[70:200])
    numbers = [num for num in numbers[70:200] if num > min_num1]
    if len(numbers) == 0:
        return None
    min_num2 = min(numbers)
    return min_num2