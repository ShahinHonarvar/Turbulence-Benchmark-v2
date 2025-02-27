def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[13:69]) < 2:
        return None
    min_num, second_min_num = (float('inf'), float('inf'))
    for num in numbers[13:69]:
        if num < min_num:
            second_min_num = min_num
            min_num = num
        elif second_min_num > num > min_num:
            second_min_num = num
    return second_min_num if second_min_num != float('inf') else None