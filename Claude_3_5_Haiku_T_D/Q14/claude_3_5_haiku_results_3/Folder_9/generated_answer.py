def find_second_smallest_num(numbers):
    if not numbers or len(numbers) < 71:
        return None
    subset = numbers[70:201]
    if not subset:
        return None
    try:
        sorted_subset = sorted(set(subset))
        return sorted_subset[1] if len(sorted_subset) > 1 else None
    except:
        return None