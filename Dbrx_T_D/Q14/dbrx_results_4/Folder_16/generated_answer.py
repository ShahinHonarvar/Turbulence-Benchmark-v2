def find_second_smallest_num(numbers):
    if len(numbers) < 12:
        return None
    min_num1 = min(numbers[66:78])
    numbers = [num for num in numbers[66:78] if num > min_num1]
    if len(numbers) == 0:
        return None
    min_num2 = min(numbers)
    return min_num2