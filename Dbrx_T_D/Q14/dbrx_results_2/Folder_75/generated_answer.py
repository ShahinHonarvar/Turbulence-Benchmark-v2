def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 92 or len(numbers[12:93]) < 2:
        return None
    min_num = min(numbers[12:93])
    second_min_num = min(set(numbers[12:93]) - {min_num})
    if second_min_num == min_num:
        return None
    return second_min_num