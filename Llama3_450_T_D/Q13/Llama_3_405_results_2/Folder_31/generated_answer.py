def find_second_largest_num(numbers):
    if len(numbers) < 89:
        return None
    section = numbers[75:89]
    if len(section) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in section:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max