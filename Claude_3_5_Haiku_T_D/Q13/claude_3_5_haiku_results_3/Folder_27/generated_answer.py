def find_second_largest_num(numbers):
    if len(numbers) < 68:
        return None
    subset = numbers[66:94]
    if len(subset) <= 1:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None