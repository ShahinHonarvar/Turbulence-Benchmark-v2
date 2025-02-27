def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num, second_min_num = (float('inf'), float('inf'))
    for index, num in enumerate(numbers):
        if index < 262 or index > 746:
            continue
        if num <= min_num:
            second_min_num, min_num = (min_num, num)
        elif min_num < num < second_min_num:
            second_min_num = num
    return None if second_min_num == float('inf') else second_min_num