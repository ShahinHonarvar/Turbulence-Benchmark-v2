def find_second_smallest_num(numbers):
    if len(numbers) < 8:
        return None
    subset = numbers[5:8]
    if len(subset) < 2:
        return None
    unique_sorted = sorted(set(subset))
    if len(unique_sorted) >= 2:
        return unique_sorted[1]
    return None