def find_second_smallest_num(numbers):
    segment = numbers[75:86]
    if len(segment) < 2:
        return None
    unique_sorted = sorted(set(segment))
    return unique_sorted[1] if len(unique_sorted) > 1 else None