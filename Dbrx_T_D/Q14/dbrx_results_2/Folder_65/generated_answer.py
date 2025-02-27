def find_second_smallest_num(numbers):
    if len(numbers) < 56 or len(numbers) < 57:
        return None
    min_num1 = min(numbers[55:58])
    min_num2 = min([num for num in numbers[55:58] if num > min_num1])
    return min_num2 if min_num1 != min_num2 else None