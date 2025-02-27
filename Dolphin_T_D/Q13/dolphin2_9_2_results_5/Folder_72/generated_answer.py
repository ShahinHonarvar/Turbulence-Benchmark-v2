def find_second_largest_num(numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[29]
    second_max_num = float('-inf')
    for i in range(30, 52):
        if numbers[i] > max_num:
            second_max_num = max_num
            max_num = numbers[i]
        elif numbers[i] > second_max_num and numbers[i] != max_num:
            second_max_num = numbers[i]
    if second_max_num == float('-inf'):
        return None
    else:
        return second_max_num