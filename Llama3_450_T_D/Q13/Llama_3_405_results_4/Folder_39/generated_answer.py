def find_second_largest_num(numbers):
    if not numbers:
        return None
    if len(numbers) < 31:
        return None
    numbers = numbers[20:31]
    if len(numbers) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in numbers:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num