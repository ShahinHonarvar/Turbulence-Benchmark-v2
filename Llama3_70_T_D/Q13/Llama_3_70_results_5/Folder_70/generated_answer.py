def find_second_largest_num(numbers):
    if len(numbers) < 33:
        return None
    second_max = float('-inf')
    max_num = float('-inf')
    for num in numbers[28:33]:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    return second_max if second_max != float('-inf') else None