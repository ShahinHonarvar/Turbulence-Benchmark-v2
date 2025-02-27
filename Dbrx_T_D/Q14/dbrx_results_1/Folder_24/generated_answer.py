def find_second_smallest_num(numbers):
    if len(numbers) < 23 * 2:
        return None
    first_smallest_num = min(numbers[23:])
    second_smallest_num = float('inf')
    for num in numbers[23:]:
        if num > first_smallest_num and num < second_smallest_num:
            second_smallest_num = num
    return second_smallest_num if second_smallest_num < float('inf') else None