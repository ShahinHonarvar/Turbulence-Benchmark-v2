def find_second_smallest_num(numbers):
    if not numbers or len(numbers) <= 66:
        return None
    subset = numbers[66:78]
    if not subset:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1] if len(sorted_subset) > 1 else None