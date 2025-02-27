def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = min(numbers[:5])
    second_num = float('inf')
    for num in numbers[:5]:
        if num > min_num and num < second_num:
            second_num = num
    if second_num == float('inf'):
        return None
    else:
        return second_num