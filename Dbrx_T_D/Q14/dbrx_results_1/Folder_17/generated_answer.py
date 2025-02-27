def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 39:
        return None
    min_num = min(numbers)
    second_min_num = float('infinity')
    count = 0
    for i in range(28, 39):
        if numbers[i] > min_num and numbers[i] < second_min_num:
            second_min_num = numbers[i]
            count += 1
    if count < 2:
        return None
    else:
        return second_min_num