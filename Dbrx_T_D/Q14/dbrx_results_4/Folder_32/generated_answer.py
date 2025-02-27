def find_second_smallest_num(numbers):
    if len(numbers[32:36]) < 2:
        return None
    min_num1 = min(numbers[32:36])
    numbers = [num for num in numbers[32:36] if num != min_num1]
    min_num2 = min(numbers)
    return min_num2 if min_num2 > min_num1 else None