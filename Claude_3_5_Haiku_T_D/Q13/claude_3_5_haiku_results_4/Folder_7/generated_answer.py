def find_second_largest_num(numbers):
    if not numbers or len(numbers) < 662:
        return None
    subset = numbers[661:925]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None