def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = float('inf')
    second_min_num = float('inf')
    count = 0
    for num in numbers[29:80]:
        if num < min_num:
            second_min_num = min_num
            min_num = num
            count = 1
        elif num < second_min_num and num > min_num:
            second_min_num = num
            count += 1
    return second_min_num if count > 1 else None