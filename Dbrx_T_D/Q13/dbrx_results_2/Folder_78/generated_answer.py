def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = max_num = numbers[43]
    second_max_num = None
    for i in range(44, 52):
        if numbers[i] > max_num:
            second_max_num = max_num
            max_num = numbers[i]
        elif numbers[i] < min_num:
            min_num = numbers[i]
        elif numbers[i] > min_num and (second_max_num is None or numbers[i] > second_max_num):
            second_max_num = numbers[i]
    if second_max_num is not None and second_max_num < max_num:
        return second_max_num
    else:
        return None