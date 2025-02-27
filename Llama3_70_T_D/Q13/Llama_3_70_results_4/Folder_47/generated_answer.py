def find_second_largest_num(numbers):
    if len(numbers) < 77:
        return None
    second_largest = float('-inf')
    max_num = float('-inf')
    for num in numbers[37:77]:
        if num > max_num:
            second_largest = max_num
            max_num = num
        elif num > second_largest and num != max_num:
            second_largest = num
    if second_largest == float('-inf'):
        return None
    return second_largest