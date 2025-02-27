def find_second_smallest_num(numbers):
    subset = numbers[20:31]
    if len(subset) < 2:
        return None
    unique_sorted = sorted(set(subset))
    if len(unique_sorted) < 2:
        return None
    return unique_sorted[1]