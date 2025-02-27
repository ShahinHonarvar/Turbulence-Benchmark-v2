def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    max_num = second_max = float('-inf')
    for i in range(9):
        if i >= len(numbers):
            break
        if numbers[i] > max_num:
            second_max = max_num
            max_num = numbers[i]
        elif numbers[i] > second_max and numbers[i] != max_num:
            second_max = numbers[i]
    if second_max == float('-inf'):
        return None
    return second_max