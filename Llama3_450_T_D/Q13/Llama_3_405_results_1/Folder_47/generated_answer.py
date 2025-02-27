def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    slice_ = numbers[37:77]
    if len(slice_) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in slice_:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    if second_max == float('-inf'):
        return None
    return second_max