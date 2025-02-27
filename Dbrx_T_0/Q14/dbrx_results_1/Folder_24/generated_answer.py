def find_second_smallest_num(numbers):
    if len(numbers) < 23 or len(numbers) < 24:
        return None
    min_num = min(numbers[23:24])
    second_min_num = float('inf')
    for num in numbers[23:24]:
        if num > min_num and num < second_min_num:
            second_min_num = num
    if second_min_num == float('inf'):
        return None
    else:
        return second_min_num