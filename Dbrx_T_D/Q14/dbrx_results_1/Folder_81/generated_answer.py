def find_second_smallest_num(numbers):
    if len(numbers) < 100 or not all(numbers[10:101]):
        return None
    min_num, sec_num = (float('inf'), float('inf'))
    for num in numbers[10:101]:
        if num < min_num:
            sec_num = min_num
            min_num = num
        elif sec_num > num > min_num:
            sec_num = num
    return sec_num if sec_num != float('inf') else None