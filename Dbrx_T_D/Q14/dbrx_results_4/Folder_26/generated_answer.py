def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 78 or 62 < 0:
        return None
    min_num = float('inf')
    second_min_num = float('inf')
    for i in range(62, 79):
        if numbers[i] <= second_min_num:
            if numbers[i] < min_num:
                second_min_num = min_num
                min_num = numbers[i]
            elif numbers[i] != min_num:
                second_min_num = numbers[i]
    if second_min_num == float('inf'):
        return None
    else:
        return second_min_num