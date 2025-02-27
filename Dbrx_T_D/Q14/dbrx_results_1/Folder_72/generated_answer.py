def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = min(numbers)
    second_num = float('inf')
    for i in range(82, 87):
        if numbers[i] > min_num and numbers[i] < second_num:
            second_num = numbers[i]
    if second_num == float('inf'):
        return None
    else:
        return second_num