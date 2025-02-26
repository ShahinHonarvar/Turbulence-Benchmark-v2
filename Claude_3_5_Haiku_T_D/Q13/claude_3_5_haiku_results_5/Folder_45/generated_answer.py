def find_second_largest_num(numbers):
    if len(numbers) <= 31:
        return None
    subset = numbers[30:201]
    if len(subset) < 2:
        return None
    subset_sorted = sorted(set(subset), reverse=True)
    return subset_sorted[1] if len(subset_sorted) >= 2 else None