def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 66 or len(numbers) < 56:
        return None
    min_num, second_min_num = (float('inf'), float('inf'))
    for num in numbers[56:67]:
        if num < min_num:
            second_min_num = min_num
            min_num = num
        elif num < second_min_num and num > min_num:
            second_min_num = num
    if second_min_num == float('inf'):
        return None
    else:
        return second_min_num