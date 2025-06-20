def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 688:
        return None
    subset = numbers[686:988]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None