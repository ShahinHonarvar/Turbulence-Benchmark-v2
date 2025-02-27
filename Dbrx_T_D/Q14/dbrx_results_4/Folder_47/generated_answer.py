def find_second_smallest_num(numbers):
    if len(numbers) < 43:
        return None
    min_num1 = min(numbers[21:64])
    numbers = [num for num in numbers[21:64] if num > min_num1]
    if len(numbers) < 2:
        return None
    min_num2 = min(numbers[1:])
    return min_num2