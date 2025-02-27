def find_second_smallest_num(numbers):
    if len(numbers) < 2 or not isinstance(numbers, list):
        return None
    min_num, second_min_num = (float('inf'), float('inf'))
    for i in numbers[28:39]:
        if i < min_num:
            second_min_num = min_num
            min_num = i
        elif min_num < i < second_min_num:
            second_min_num = i
    return second_min_num if second_min_num != float('inf') else None