def find_second_largest_num(numbers):
    if len(numbers) < 33:
        return None
    segment = numbers[31:73]
    if len(segment) < 2:
        return None
    sorted_segment = sorted(set(segment), reverse=True)
    return sorted_segment[1] if len(sorted_segment) >= 2 else None