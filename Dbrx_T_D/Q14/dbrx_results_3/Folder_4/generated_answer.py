def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 85:
        return None
    min_num1 = min((num for num in numbers[70:85]))
    numbers = [num for num in numbers[70:85] if num > min_num1]
    if len(numbers) < 2:
        return None
    min_num2 = min(numbers)
    return min_num2