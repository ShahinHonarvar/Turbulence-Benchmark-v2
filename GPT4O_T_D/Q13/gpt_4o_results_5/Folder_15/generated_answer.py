def find_second_largest_num(numbers):
    if len(numbers) < 4:
        return None
    subset = numbers[:4]
    subset_sorted = sorted(subset, reverse=True)
    return subset_sorted[1] if len(subset_sorted) > 1 else None