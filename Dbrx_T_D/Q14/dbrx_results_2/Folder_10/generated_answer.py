def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 92 - 62 + 1 < 2:
        return None
    min_num = min(numbers[62:93])
    second_min_num = float('inf')
    for num in numbers[62:93]:
        if num > min_num and num < second_min_num:
            second_min_num = num
    return second_min_num if second_min_num < float('inf') else None