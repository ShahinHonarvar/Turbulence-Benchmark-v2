def find_second_largest_num(numbers):
    if len(numbers) < 56:
        return None
    subset = numbers[55:99]
    if len(subset) < 2:
        return None
    unique_subset = sorted(set(subset), reverse=True)
    if len(unique_subset) < 2:
        return None
    return unique_subset[1]