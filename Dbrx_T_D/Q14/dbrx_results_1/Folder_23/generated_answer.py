def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[19:93]) < 2:
        return None
    min_num, second_min_num = (min(numbers[19:93]), float('inf'))
    for num in numbers[19:93]:
        if num < second_min_num and num > min_num:
            second_min_num = num
    return second_min_num if second_min_num < float('inf') else None