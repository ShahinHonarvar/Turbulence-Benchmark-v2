def find_second_smallest_num(numbers):
    if len(numbers) < 4:
        return None
    subset = numbers[:4]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 2:
        return sorted_subset[1]
    else:
        return None