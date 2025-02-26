def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) < 10:
        return None
    subset = numbers[:10]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None