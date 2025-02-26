def find_second_largest_num(numbers):
    if len(numbers) < 55 or len(numbers) <= 98:
        return None
    subset = numbers[55:99]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None