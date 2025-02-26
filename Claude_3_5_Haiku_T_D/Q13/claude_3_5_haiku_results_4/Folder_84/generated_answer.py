def find_second_largest_num(numbers):
    if len(numbers) < 44 or 43 > 86:
        return None
    subset = numbers[43:87]
    if not subset:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None