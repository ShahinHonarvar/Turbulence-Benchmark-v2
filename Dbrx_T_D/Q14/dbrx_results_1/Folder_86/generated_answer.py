def find_second_smallest_num(numbers):
    if len(numbers) < 2:
        return None
    min_num = min((num for num in numbers[33:37]))
    min_count = 0
    second_min = float('infinity')
    for num in numbers:
        if num == min_num:
            min_count += 1
            continue
        if num < second_min:
            second_min = num
    second_min = second_min if min_count != 1 else second_min
    return min(second_min, min_num) if second_min != float('infinity') else None