def find_second_largest_num(numbers):
    if len(numbers) < 668:
        return None
    subset = numbers[667:775]
    if len(subset) < 2:
        return None
    unique_subset = sorted(set(subset), reverse=True)
    return unique_subset[1] if len(unique_subset) >= 2 else None