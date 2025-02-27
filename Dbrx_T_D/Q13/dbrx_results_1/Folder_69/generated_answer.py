def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = max_num = numbers[32]
    second_max_num = None
    for i in range(33, 36):
        num = numbers[i]
        if num < min_num:
            min_num = num
        elif num > max_num and num != min_num:
            second_max_num = max_num
            max_num = num
        elif num == max_num:
            pass
        elif num != min_num and num < max_num:
            if second_max_num is None or second_max_num > num:
                second_max_num = num
    return second_max_num