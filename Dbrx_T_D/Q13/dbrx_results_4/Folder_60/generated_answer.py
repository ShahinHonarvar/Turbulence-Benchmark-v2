def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = max_num = numbers[75]
    second_max_num = None
    for i in range(76, 86):
        num = numbers[i]
        if num < min_num:
            if num > second_max_num:
                second_max_num = num
        elif num > max_num and num != min_num:
            second_max_num, max_num = (max_num, num)
    return second_max_num if second_max_num is not None and second_max_num != max_num else None