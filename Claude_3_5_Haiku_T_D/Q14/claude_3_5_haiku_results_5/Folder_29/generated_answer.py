def find_second_smallest_num(numbers):
    if len(numbers) < 55 or len(numbers) < 98:
        return None
    subset = numbers[55:99]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset))
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]