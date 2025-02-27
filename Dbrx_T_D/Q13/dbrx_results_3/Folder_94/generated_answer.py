def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = max_num = numbers[28]
    count = 0
    for i in range(28, 41):
        if numbers[i] > max_num:
            max_num = numbers[i]
            count += 1
        elif numbers[i] < min_num:
            min_num = numbers[i]
    if count < 2:
        return None
    second_max_num = min_num
    for i in range(28, 41):
        if numbers[i] > min_num and numbers[i] < max_num:
            second_max_num = numbers[i]
    return second_max_num