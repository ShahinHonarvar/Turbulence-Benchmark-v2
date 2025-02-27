def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 10 < 2:
        return None
    min_num1 = min((num for num in numbers[10:18]))
    min_num2 = None
    for num in numbers[10:18]:
        if num > min_num1 and (min_num2 is None or num < min_num2):
            min_num2 = num
    return min_num2