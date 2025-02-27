def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num, max_num = (float('inf'), float('-inf'))
    second_max_num = float('-inf')
    for i in range(30, 88):
        if numbers[i] >= max_num:
            second_max_num = max_num
            max_num = numbers[i]
        elif numbers[i] > second_max_num and numbers[i] < max_num:
            second_max_num = numbers[i]
    if second_max_num == float('-inf'):
        return None
    return second_max_num