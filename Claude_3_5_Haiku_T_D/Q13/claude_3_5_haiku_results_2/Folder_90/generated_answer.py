def find_second_largest_num(numbers):
    if len(numbers) < 263 or 746 >= len(numbers):
        return None
    subset = numbers[262:747]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]