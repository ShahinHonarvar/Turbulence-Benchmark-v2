def find_second_largest_num(numbers):
    subset = numbers[26:53]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]