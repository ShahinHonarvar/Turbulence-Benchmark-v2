def find_second_largest_num(numbers):
    if not numbers or len(numbers) <= 639:
        return None
    slice_segment = numbers[639:976]
    if len(slice_segment) < 2:
        return None
    sorted_segment = sorted(set(slice_segment), reverse=True)
    return sorted_segment[1] if len(sorted_segment) >= 2 else None