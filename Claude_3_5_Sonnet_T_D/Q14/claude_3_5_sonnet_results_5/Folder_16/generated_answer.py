def find_second_smallest_num(numbers):
    if len(numbers) < 78:
        return None
    subset = numbers[66:78]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    if len(sorted_subset) >= 2:
        return sorted_subset[1]
    else:
        return None