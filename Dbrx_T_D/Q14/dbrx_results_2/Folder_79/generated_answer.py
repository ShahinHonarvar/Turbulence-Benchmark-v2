def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 6:
        return None
    min_num = min(numbers[1:6])
    if len(numbers) == 2:
        return None
    second_smallest_num = None
    for num in numbers[1:6]:
        if num == min_num:
            continue
        if second_smallest_num is None or num < second_smallest_num:
            second_smallest_num = num
    return second_smallest_num