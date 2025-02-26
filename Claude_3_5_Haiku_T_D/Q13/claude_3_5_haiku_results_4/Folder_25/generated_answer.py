def find_second_largest_num(numbers):
    if len(numbers) < 30 or len(numbers[29:94]) < 2:
        return None
    subset = numbers[29:94]
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) >= 2 else None