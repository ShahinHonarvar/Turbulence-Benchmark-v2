def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 66 or len(numbers) < 93:
        return None
    min_num1 = min(numbers[66:94])
    numbers = [num for num in numbers if num > min_num1]
    if len(numbers) < 2:
        return None
    min_num2 = min(numbers[66:94])
    return min_num2