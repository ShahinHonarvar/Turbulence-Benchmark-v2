def find_second_largest_num(numbers):
    if len(numbers) <= 1 or len(numbers) < 11:
        return None
    subset = numbers[:11]
    sorted_subset = sorted(set(subset), reverse=True)
    return sorted_subset[1] if len(sorted_subset) > 1 else None