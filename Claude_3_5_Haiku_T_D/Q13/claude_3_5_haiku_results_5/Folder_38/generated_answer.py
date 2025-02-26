def find_second_largest_num(numbers):
    if len(numbers) < 64:
        return None
    subset = numbers[22:64]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None