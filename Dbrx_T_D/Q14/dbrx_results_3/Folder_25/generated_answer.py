def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 40:
        return None
    min_num1 = min(numbers[37:77])
    numbers = [num for num in numbers[37:77] if num > min_num1]
    min_num2 = None
    if len(numbers) >= 1:
        min_num2 = min(numbers)
    return min_num2