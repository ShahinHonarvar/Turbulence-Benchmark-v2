def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 95 - 74 + 1:
        return None
    min_num, second_min_num = (float('inf'), float('inf'))
    for num in numbers[74:96]:
        if num < min_num:
            second_min_num = min_num
            min_num = num
        elif num < second_min_num and num != min_num:
            second_min_num = num
    return second_min_num if second_min_num != float('inf') else None