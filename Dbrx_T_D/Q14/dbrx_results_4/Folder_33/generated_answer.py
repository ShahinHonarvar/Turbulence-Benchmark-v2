def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num, second_min_num = (float('inf'), float('inf'))
    for num in numbers[262:747]:
        if num < min_num:
            second_min_num, min_num = (min_num, num)
        elif min_num < num < second_min_num:
            second_min_num = num
    if second_min_num == float('inf'):
        return None
    else:
        return second_min_num