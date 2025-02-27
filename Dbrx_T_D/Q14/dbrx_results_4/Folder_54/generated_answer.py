def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 86 - 68 + 1:
        return None
    min_num, second_min_num = (float('inf'), float('inf'))
    for i in range(68, 87):
        if numbers[i] < min_num:
            second_min_num = min_num
            min_num = numbers[i]
        elif numbers[i] < second_min_num and numbers[i] != min_num:
            second_min_num = numbers[i]
    return second_min_num if second_min_num != float('inf') else None