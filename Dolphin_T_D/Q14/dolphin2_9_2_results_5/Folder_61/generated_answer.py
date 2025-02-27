def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    smallest_num = float('inf')
    second_smallest_num = float('inf')
    for i in range(8):
        if numbers[i] < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = numbers[i]
        elif numbers[i] < second_smallest_num and numbers[i] != smallest_num:
            second_smallest_num = numbers[i]
    if second_smallest_num == float('inf'):
        return None
    else:
        return second_smallest_num