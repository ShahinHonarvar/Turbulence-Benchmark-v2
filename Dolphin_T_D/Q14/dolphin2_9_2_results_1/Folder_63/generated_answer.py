def find_second_smallest_num(numbers):
    if len(numbers) < 82:
        return None
    subset = numbers[56:82 + 1]
    if len(set(subset)) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1]