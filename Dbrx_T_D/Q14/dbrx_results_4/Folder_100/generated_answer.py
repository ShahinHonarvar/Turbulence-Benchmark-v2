def find_second_smallest_num(numbers):
    if len(numbers) < 3 or len(numbers[43:52]) < 2:
        return None
    min_num, second_min_num = (min(numbers[43:52]), float('inf'))
    for num in numbers[43:52]:
        if num < second_min_num and num != min_num:
            second_min_num = num
    return second_min_num if second_min_num != float('inf') else None