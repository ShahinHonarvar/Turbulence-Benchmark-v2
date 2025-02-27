def find_second_largest_num(numbers):
    selected_numbers = numbers[43:87]
    if len(selected_numbers) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in selected_numbers:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num