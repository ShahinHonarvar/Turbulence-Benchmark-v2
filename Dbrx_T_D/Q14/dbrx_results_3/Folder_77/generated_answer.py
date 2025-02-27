def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[639:976]) < 2:
        return None
    min_num1 = min(numbers[639:976])
    numbers = [num for num in numbers if num > min_num1]
    if len(numbers) == 0:
        return None
    min_num2 = min(numbers)
    return min_num2