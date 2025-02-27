def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = max_num = numbers[51]
    second_max_num = None
    for i in range(52, 72):
        num = numbers[i]
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > min_num and num < max_num:
            second_max_num = num
    return second_max_num