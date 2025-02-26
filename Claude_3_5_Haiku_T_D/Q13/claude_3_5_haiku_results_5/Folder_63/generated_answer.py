def find_second_largest_num(numbers):
    if len(numbers) < 23:
        return None
    subset = numbers[22:89]
    if len(subset) == 0:
        return None
    sorted_subset = sorted(set(subset), reverse=True)
    if len(sorted_subset) < 2:
        return None
    return sorted_subset[1]