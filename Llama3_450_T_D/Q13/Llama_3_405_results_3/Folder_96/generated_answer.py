def find_second_largest_num(num_list):
    if len(num_list) < 52:
        return None
    numbers = num_list[15:52]
    if len(numbers) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in numbers:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max