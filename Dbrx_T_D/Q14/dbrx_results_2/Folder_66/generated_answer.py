def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 37:
        return None
    min_num = float('inf')
    second_min_num = float('inf')
    for i in range(62, 100):
        if numbers[i] < min_num:
            second_min_num = min_num
            min_num = numbers[i]
        elif numbers[i] > min_num and numbers[i] < second_min_num:
            second_min_num = numbers[i]
    return second_min_num if len(set(numbers[62:100])) > 1 else None