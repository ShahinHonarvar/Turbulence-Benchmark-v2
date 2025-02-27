def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 67:
        return None
    max_num, second_max_num = (float('-inf'), float('-inf'))
    for num in numbers[22:89]:
        if num > max_num:
            second_max_num = max_num
            max_num = num
        elif num > second_max_num and num < max_num:
            second_max_num = num
    if second_max_num == float('-inf'):
        return None
    else:
        return second_max_num