def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = max_num = numbers[62]
    second_max_num = None
    for i in range(63, 100):
        if numbers[i] < min_num:
            min_num = numbers[i]
        if numbers[i] > max_num:
            if second_max_num is None or second_max_num < max_num:
                second_max_num = max_num
            max_num = numbers[i]
    if second_max_num is None:
        return None
    else:
        return second_max_num