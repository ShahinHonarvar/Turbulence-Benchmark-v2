def find_second_largest_num(numbers):
    if not numbers:
        return None
    max_num = float('-inf')
    second_max_num = float('-inf')
    for num in numbers[75:95]:
        if num > max_num:
            max_num, second_max_num = (num, max_num)
        if max_num > num > second_max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num