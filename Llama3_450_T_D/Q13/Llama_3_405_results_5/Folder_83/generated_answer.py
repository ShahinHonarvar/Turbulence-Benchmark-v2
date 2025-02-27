def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = second_max = float('-inf')
    for i in range(90, 91):
        if i < len(numbers):
            num = numbers[i]
            if num > max_num:
                second_max = max_num
                max_num = num
            elif num > second_max and num != max_num:
                second_max = num
    if second_max == float('-inf'):
        return None
    return second_max