def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('inf')
    second_min_num = float('inf')
    for i in range(310, 371):
        if i >= len(numbers):
            return None
        if numbers[i] < min_num:
            second_min_num = min_num
            min_num = numbers[i]
        elif min_num < numbers[i] < second_min_num:
            second_min_num = numbers[i]
    if second_min_num == float('inf'):
        return None
    else:
        return second_min_num