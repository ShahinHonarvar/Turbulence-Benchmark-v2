def find_second_largest_num(numbers):
    if len(numbers) < 6:
        return None
    subset = numbers[1:6]
    if len(set(subset)) < 2:
        return None
    sorted_subset = sorted(subset, reverse=True)
    return sorted_subset[1]