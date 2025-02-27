def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = min(numbers[:2])
    second_num = max(numbers[:2])
    for num in numbers[2:]:
        if num < min_num:
            second_num = min_num
            min_num = num
        elif num < second_num and num != min_num:
            second_num = num
    return second_num if second_num != min_num else None