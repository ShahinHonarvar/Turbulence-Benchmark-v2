def find_second_largest_num(numbers):
    specified_range = numbers[28:41]
    if len(specified_range) < 2:
        return None
    max_num = second_max = float('-inf')
    for num in specified_range:
        if num > max_num:
            second_max = max_num
            max_num = num
        elif num > second_max and num != max_num:
            second_max = num
    return second_max if second_max != float('-inf') else None