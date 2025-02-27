def find_second_smallest_num(numbers):
    subset = numbers[10:67]
    if len(subset) < 2:
        return None
    unique_subset = sorted(set(subset))
    if len(unique_subset) < 2:
        return None
    return unique_subset[1]