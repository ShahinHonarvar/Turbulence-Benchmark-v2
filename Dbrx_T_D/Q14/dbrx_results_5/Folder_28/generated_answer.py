def find_second_smallest_num(numbers):
    if len(numbers) < 50 or len(numbers) < 22:
        return None
    min_num1 = min((num for num in numbers[22:50]))
    numbers = [num for num in numbers[22:50] if num != min_num1]
    if len(numbers) < 1:
        return None
    min_num2 = min(numbers)
    return min_num2 if min_num2 != min_num1 else None