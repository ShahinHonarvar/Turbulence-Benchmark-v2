def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    if len(numbers[62:93]) < 2:
        return None
    min_num, second_min_num = (min(numbers[62:93]), float('inf'))
    for num in numbers[62:93]:
        if num == min_num:
            continue
        if num < second_min_num:
            second_min_num = num
    if second_min_num != float('inf'):
        return second_min_num
    return None