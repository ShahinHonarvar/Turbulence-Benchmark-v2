def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 51 - 37 + 1:
        return None
    min_num = min(numbers[37:52])
    second_min_num = float('inf')
    for num in numbers[37:52]:
        if num > min_num and num < second_min_num:
            second_min_num = num
    return second_min_num if second_min_num != float('inf') else None