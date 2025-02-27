def find_second_smallest_num(numbers):
    if len(numbers) < 2 or 55 - 27 + 1 < 2:
        return None
    start_index = 27
    end_index = 55
    min_num = min(numbers[start_index:end_index + 1])
    second_min_num = float('inf')
    found_min = False
    for num in numbers[start_index:end_index + 1]:
        if num == min_num:
            continue
        if num < second_min_num:
            second_min_num = num
            found_min = True
    return second_min_num if found_min else None