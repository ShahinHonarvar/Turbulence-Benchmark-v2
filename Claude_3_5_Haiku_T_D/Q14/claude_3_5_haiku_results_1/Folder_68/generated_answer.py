def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 9:
        return None
    subset = numbers[:9]
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 2:
        return sorted_subset[1]
    else:
        return None