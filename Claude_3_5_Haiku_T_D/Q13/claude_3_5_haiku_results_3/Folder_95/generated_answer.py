def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 84:
        return None
    segment = numbers[82:87]
    if len(segment) < 2:
        return None
    sorted_segment = sorted(set(segment), reverse=True)
    return sorted_segment[1] if len(sorted_segment) > 1 else None