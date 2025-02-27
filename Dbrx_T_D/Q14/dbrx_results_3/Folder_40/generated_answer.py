def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    min_num1 = min(numbers[0], numbers[1])
    min_num2 = max(numbers[0], numbers[1])
    for num in numbers[2:]:
        if num < min_num1:
            min_num2 = min_num1
            min_num1 = num
        elif num < min_num2:
            min_num2 = num
    if min_num2 == numbers[0] or min_num2 == numbers[1] or min_num2 == numbers[2]:
        return min_num2
    return None