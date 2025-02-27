def find_second_smallest_num(numbers):
    if len(numbers) < 7:
        return None
    min_num = min(numbers[6:7])
    second_min_num = float('inf')
    count = 0
    for i in range(6, len(numbers)):
        if numbers[i] == min_num:
            continue
        elif numbers[i] < second_min_num:
            second_min_num = numbers[i]
            count += 1
    if count < 2:
        return None
    else:
        return second_min_num