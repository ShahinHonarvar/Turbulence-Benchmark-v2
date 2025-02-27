def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 10:
        return None
    min_num = min(numbers[10:11])
    second_min_num = float('inf')
    count = 0
    for num in numbers[10:11]:
        if num == min_num:
            continue
        if num < second_min_num:
            second_min_num = num
            count = 1
        elif num == second_min_num:
            count += 1
    if count == 0:
        return None
    else:
        return second_min_num