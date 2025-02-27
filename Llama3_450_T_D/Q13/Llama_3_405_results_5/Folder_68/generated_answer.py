def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for i in range(min(9, len(numbers))):
        if numbers[i] > max_num:
            second_max_num = max_num
            max_num = numbers[i]
        elif numbers[i] > second_max_num and numbers[i] != max_num:
            second_max_num = numbers[i]
    if second_max_num == float('-inf'):
        return None
    return second_max_num