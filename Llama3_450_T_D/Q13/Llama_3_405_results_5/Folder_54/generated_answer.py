def find_second_largest_num(numbers):
    specified_range = numbers[34:56]
    if len(specified_range) < 2:
        return None
    max_num = second_max_num = float('-inf')
    for num in specified_range:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num != max_num:
            second_max_num = num
    return second_max_num if second_max_num != float('-inf') else None