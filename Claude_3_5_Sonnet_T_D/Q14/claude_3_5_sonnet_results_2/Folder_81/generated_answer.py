def find_second_smallest_num(numbers):
    if len(numbers) < 11:
        return None
    target_range = numbers[10:101]
    if len(target_range) < 2:
        return None
    sorted_range = sorted(set(target_range))
    if len(sorted_range) < 2:
        return None
    return sorted_range[1]