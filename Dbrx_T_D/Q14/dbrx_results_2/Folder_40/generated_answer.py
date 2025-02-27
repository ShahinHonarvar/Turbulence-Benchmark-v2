def find_second_smallest_num(numbers):
    if len(numbers) < 3:
        return None
    min_num = min(numbers[:3])
    second_min_num = float('inf')
    for num in numbers[:3]:
        if num > min_num and num < second_min_num:
            second_min_num = num
    if second_min_num == float('inf'):
        return None
    else:
        return second_min_num