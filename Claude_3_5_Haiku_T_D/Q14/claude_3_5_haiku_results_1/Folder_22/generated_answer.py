def find_second_smallest_num(numbers):
    if len(numbers) <= 41:
        return None
    subset = numbers[40:201]
    if len(subset) < 2:
        return None
    unique_subset = list(set(subset))
    if len(unique_subset) < 2:
        return None
    unique_subset.sort()
    return unique_subset[1]