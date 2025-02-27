def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = max_num = numbers[12]
    second_max_num = None
    for i in range(13, 93):
        if numbers[i] > max_num:
            second_max_num = max_num
            max_num = numbers[i]
        elif numbers[i] > min_num and numbers[i] < max_num:
            second_max_num = numbers[i]
    if second_max_num is None:
        return None
    else:
        return second_max_num