def find_second_largest_num(numbers):
    if len(numbers) < 66:
        return None
    subset = numbers[14:65]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]