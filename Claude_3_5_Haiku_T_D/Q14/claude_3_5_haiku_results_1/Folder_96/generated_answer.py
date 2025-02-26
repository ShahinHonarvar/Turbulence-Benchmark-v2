def find_second_smallest_num(numbers):
    if len(numbers) < 252:
        return None
    subset = numbers[50:201]
    if not subset:
        return None
    sorted_subset = sorted(set(subset))
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]