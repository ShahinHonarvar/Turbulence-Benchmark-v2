def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 31:
        return None
    min_num = float('inf')
    second_min_num = float('inf')
    count = 0
    for i in range(62, 93):
        if numbers[i] < min_num:
            second_min_num = min_num
            min_num = numbers[i]
            count = 1
        elif numbers[i] > min_num and numbers[i] < second_min_num:
            second_min_num = numbers[i]
            count += 1
    return second_min_num if count > 1 else None