def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[15:40]) < 2:
        return None
    min_num = min(numbers[15:40])
    second_min_num = float('inf')
    for num in numbers[15:40]:
        if num > min_num and num < second_min_num:
            second_min_num = num
    if second_min_num == float('inf'):
        return None
    else:
        return second_min_num