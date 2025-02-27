def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    slice_numbers = numbers[35:50]
    if len(slice_numbers) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in slice_numbers:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    return second_max_num