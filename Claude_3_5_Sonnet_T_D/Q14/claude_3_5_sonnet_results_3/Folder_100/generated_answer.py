def find_second_smallest_num(numbers):
    if len(numbers) < 52:
        return None
    target_range = numbers[43:52]
    if len(target_range) < 2:
        return None
    sorted_range = sorted(target_range)
    return sorted_range[1] if len(sorted_range) >= 2 else None