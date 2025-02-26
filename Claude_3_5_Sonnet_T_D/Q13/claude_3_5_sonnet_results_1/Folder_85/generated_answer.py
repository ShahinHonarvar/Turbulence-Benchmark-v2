def find_second_largest_num(numbers):
    if len(numbers) < 9:
        return None
    subset = numbers[6:9]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None