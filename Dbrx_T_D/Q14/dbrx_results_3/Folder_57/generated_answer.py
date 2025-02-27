def find_second_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    min_num = float('inf')
    second_min_num = float('inf')
    for num in numbers[20:31]:
        if num < min_num:
            second_min_num = min_num
            min_num = num
        elif num > min_num and num < second_min_num:
            second_min_num = num
    if second_min_num == float('inf'):
        return None
    else:
        return second_min_num