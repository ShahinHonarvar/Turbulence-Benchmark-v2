def find_second_largest_num(numbers):
    if len(numbers) < 92:
        return None
    subset = numbers[91:100]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]