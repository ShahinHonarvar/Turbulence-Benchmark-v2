def find_second_largest_num(numbers):
    subset = numbers[75:86]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None