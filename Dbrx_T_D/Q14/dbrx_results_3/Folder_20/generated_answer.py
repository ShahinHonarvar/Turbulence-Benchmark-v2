def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 95 > len(numbers):
        return None
    min_num, second_min_num = (float('inf'), float('inf'))
    for num in numbers[75:95]:
        if num < min_num:
            second_min_num = min_num
            min_num = num
        elif num > min_num and num < second_min_num:
            second_min_num = num
    return second_min_num if second_min_num != float('inf') else None