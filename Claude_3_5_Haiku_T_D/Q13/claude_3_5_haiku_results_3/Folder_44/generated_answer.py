def find_second_largest_num(numbers):
    if len(numbers) < 14 or len(numbers) <= 68:
        return None
    subset = numbers[13:69]
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None