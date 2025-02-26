def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 535:
        return None
    subset = numbers[533:606]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]