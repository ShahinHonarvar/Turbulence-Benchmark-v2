def find_second_smallest_num(numbers):
    if len(numbers) < 540:
        return None
    subset = numbers[527:539]
    if not subset:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1] if len(sorted_subset) > 1 else None