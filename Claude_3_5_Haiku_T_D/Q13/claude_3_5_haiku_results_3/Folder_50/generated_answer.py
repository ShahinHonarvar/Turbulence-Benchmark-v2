def find_second_largest_num(numbers):
    if len(numbers) <= 71 or 70 > 84:
        return None
    subset = numbers[70:85]
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None