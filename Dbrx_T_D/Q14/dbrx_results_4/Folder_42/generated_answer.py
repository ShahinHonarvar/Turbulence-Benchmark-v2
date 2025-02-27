def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 98:
        return None
    min_num1 = min(numbers[20:98])
    numbers = [num for num in numbers[20:98] if num > min_num1]
    if len(numbers) < 2:
        return None
    return min(numbers[1:])