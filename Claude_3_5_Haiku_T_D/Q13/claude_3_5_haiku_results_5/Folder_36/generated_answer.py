def find_second_largest_num(numbers):
    if len(numbers) < 248 or 246 > 750:
        return None
    subset = numbers[246:751]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]