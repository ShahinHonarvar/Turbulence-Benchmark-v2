def find_second_smallest_num(numbers):
    if len(numbers) < 73:
        return None
    subset = numbers[52:72]
    if not subset:
        return None
    sorted_subset = sorted(set(subset))
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]