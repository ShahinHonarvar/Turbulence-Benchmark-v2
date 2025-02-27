def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 2 < 22 or 88 < len(numbers) - 2:
        return None
    min_num1 = min(numbers[22:89])
    min_num1_count = numbers[22:89].count(min_num1)
    numbers = [num for num in numbers[22:89] if num != min_num1]
    if not numbers:
        return None
    min_num2 = min(numbers)
    min_num2_count = numbers.count(min_num2)
    if min_num1_count < 2 and min_num2_count < 2:
        return min_num2
    elif min_num1_count < 2:
        return min_num1
    else:
        return None