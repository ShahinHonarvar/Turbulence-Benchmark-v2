def find_second_smallest_num(numbers):
    if len(numbers) < 53:
        return None
    subset = numbers[26:53]
    if len(subset) < 2:
        return None
    sorted_subset = sorted(subset)
    return sorted_subset[1]