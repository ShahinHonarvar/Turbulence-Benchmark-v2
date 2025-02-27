def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = max_num = numbers[28]
    second_max_num = None
    for i in range(28, 33):
        if numbers[i] > max_num:
            second_max_num = max_num
            max_num = numbers[i]
        elif numbers[i] > min_num and numbers[i] < max_num:
            second_max_num = numbers[i]
    return second_max_num