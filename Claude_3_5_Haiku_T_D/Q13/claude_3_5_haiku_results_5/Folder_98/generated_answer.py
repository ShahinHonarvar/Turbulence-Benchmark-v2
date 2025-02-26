def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    subset = numbers[:7]
    unique_subset = sorted(set(subset), reverse=True)
    return unique_subset[1] if len(unique_subset) > 1 else None