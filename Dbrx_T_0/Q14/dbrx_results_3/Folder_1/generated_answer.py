def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 55 or len(numbers) < 34:
        return None
    min_num1 = min(numbers[34:55])
    numbers = [num for num in numbers if num > min_num1]
    min_num2 = min(numbers[34:55])
    if min_num1 == min_num2:
        return None
    else:
        return min_num2