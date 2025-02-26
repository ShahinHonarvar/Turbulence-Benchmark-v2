def find_second_smallest_num(numbers):
    if len(numbers) < 5:
        return None
    subset = numbers[:5]
    sorted_subset = sorted(subset)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]