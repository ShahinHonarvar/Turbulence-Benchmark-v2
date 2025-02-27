def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = max_num = numbers[43]
    second_max_num = None
    for i in range(44, 87):
        if numbers[i] < min_num:
            min_num = numbers[i]
        elif numbers[i] > max_num and numbers[i] < min_num:
            second_max_num = numbers[i]
    if second_max_num is not None:
        return second_max_num
    else:
        return None