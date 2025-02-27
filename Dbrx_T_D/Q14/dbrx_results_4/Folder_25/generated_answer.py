def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 76 - 37 + 1:
        return None
    min_num1 = min(numbers[37:77])
    min_num2 = None
    for num in numbers[37:77]:
        if num > min_num1 and (num < min_num2 or min_num2 is None):
            min_num2 = num
    return min_num2