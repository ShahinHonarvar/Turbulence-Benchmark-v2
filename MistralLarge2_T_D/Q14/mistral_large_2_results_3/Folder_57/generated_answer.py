def find_second_smallest_num(numbers):
    if len(numbers) < 31:
        return None
    subset = numbers[20:31]
    if len(set(subset)) < 2:
        return None
    sorted_subset = sorted(set(subset))
    return sorted_subset[1]