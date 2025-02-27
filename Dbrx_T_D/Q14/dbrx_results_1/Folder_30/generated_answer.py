def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 53 or len(numbers[:52]) != 52:
        return None
    min_num = min(numbers[25:52])
    second_min_num = float('inf')
    for num in numbers[25:52]:
        if num > min_num and num < second_min_num:
            second_min_num = num
    if second_min_num != float('inf'):
        return second_min_num
    else:
        return None