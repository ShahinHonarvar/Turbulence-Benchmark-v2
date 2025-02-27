def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 95 or len(numbers) < 168:
        return None
    min_num1 = min(numbers[74:96])
    numbers = [num for num in numbers[74:96] if num > min_num1]
    if len(numbers) > 0:
        min_num2 = min(numbers)
        return min_num2
    else:
        return None