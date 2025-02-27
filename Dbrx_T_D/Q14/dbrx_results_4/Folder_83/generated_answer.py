def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 201 or len(numbers) < 91:
        return None
    min_num = float('inf')
    second_min_num = float('inf')
    for i in range(90, 201):
        if numbers[i] <= second_min_num:
            if numbers[i] < min_num:
                second_min_num = min_num
                min_num = numbers[i]
            elif numbers[i] > min_num:
                second_min_num = numbers[i]
    if second_min_num == float('inf'):
        return None
    else:
        return second_min_num