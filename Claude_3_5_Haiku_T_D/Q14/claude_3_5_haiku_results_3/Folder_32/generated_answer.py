def find_second_smallest_num(numbers):
    if len(numbers) < 36:
        return None
    segment = numbers[32:36]
    if len(segment) < 2:
        return None
    sorted_segment = sorted(set(segment))
    return sorted_segment[1] if len(sorted_segment) >= 2 else None