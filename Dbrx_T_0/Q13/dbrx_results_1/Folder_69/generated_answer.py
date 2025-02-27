def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = max_num = numbers[32]
    second_max_num = None
    for num in numbers[33:36]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > min_num and num < max_num:
            second_max_num = num
    return second_max_num