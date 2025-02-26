def find_second_largest_num(numbers):
    if len(numbers) < 33:
        return None
    subset = numbers[28:33]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]