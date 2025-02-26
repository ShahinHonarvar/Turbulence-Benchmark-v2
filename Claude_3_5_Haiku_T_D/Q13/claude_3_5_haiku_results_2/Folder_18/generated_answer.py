def find_second_largest_num(numbers):
    if len(numbers) < 50:
        return None
    subset = numbers[35:50]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None