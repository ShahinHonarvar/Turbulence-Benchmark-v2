def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 6:
        return None
    min_num = min(numbers[0:6])
    second_min_num = float('inf')
    for num in numbers[0:6]:
        if num > min_num and num < second_min_num:
            second_min_num = num
    if second_min_num == float('inf'):
        return None
    else:
        return second_min_num