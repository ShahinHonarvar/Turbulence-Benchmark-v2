def find_second_smallest_num(numbers):
    if len(numbers) < 93:
        return None
    segment = numbers[12:93]
    if len(segment) < 2:
        return None
    sorted_segment = sorted(set(segment))
    return sorted_segment[1] if len(sorted_segment) >= 2 else None